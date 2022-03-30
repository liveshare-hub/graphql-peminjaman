from graphene import relay, ObjectType
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import pinjam_barang, jenis_barang, daftar_barang

class JenisBarang(DjangoObjectType):
    class Meta:
        model = jenis_barang
        fields = '__all__'

# class JenisBarangMutation(graphene.Mutation):
#     class Arguments:
#         kode = graphene.String()
#         jenis = graphene.String()

#     jenisBarang = graphene.Field(JenisBarangType)

#     @classmethod
#     def mutate(cls, root, info, kode, jenis):
#         jenisBarang = jenis_barang()
#         jenisBarang.kode_jenis = kode
#         jenisBarang.nama_jenis = jenis
#         jenisBarang.save()

#         return JenisBarangMutation(jenisBarang=jenisBarang)

class CreateBarang(graphene.Mutation):
    class Arguments:
        nama = graphene.String()
        kode = graphene.String()

    barang = graphene.Field(JenisBarang)

    def mutate(root, info, nama, kode):
        barang = jenis_barang(nama_jenis=nama, kode_jenis=kode)
        barang.save()
        return CreateBarang(barang=barang)

class Barang(graphene.ObjectType):
    nama = graphene.String()
    kode = graphene.String()

class BarangMutations(graphene.ObjectType):
    buat_barang = CreateBarang.Field()

class PinjamBarangNode(DjangoObjectType):
    class Meta:
        model = pinjam_barang
        # filter_fields = ['user','tgl_pinjam']
        filter_fields = {
            'user__username':['exact','icontains','istartswith'],
            'items__kode_inventaris':['exact','icontains'],

        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    pinjam = relay.Node.Field(PinjamBarangNode)
    all_pinjam = DjangoFilterConnectionField(PinjamBarangNode)