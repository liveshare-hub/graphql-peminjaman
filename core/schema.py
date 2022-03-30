import graphene
from graphene_django import DjangoObjectType
from graphene.relay import Node

from pinjam_stock.models import jenis_barang, daftar_barang, pinjam_barang
from accounts.models import User

from pinjam_stock import schema


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id","username")

class JenisBarangType(DjangoObjectType):
    class Meta:
        model = jenis_barang
        fields = '__all__'

class DaftarBarangType(DjangoObjectType):
    class Meta:
        model = daftar_barang
        fields = '__all__'

class PinjamBarangType(DjangoObjectType):
    class Meta:
        model = pinjam_barang
        fields = '__all__'

class Query(schema.Query,graphene.ObjectType):
    all_jenisbarang = graphene.List(JenisBarangType)
    all_daftarbarang = graphene.List(DaftarBarangType)
    all_pinjambarang = graphene.List(PinjamBarangType)
    pinjambarang_by_user = graphene.List(PinjamBarangType, username=graphene.String())


    def resolve_all_jenisbarang(root, info):
        return jenis_barang.objects.all()

    def resolve_all_daftarbarang(root, info):
        return daftar_barang.objects.select_related('jenis').all()
    
    def resolve_all_pinjambarang(root, info):
        return pinjam_barang.objects.select_related('user','items').all()

    def resolve_pinjambarang_by_user(root, info, username):
        try:
            return pinjam_barang.objects.select_related('user','items').filter(user__username=username)
        except pinjam_barang.DoesNotExist:
            return None

schema = graphene.Schema(query=Query, mutation=schema.BarangMutations)