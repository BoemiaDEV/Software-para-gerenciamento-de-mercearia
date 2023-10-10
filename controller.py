from model import *
from dao import *
from datetime import datetime


class ControllerCategoria:
    def cadastracategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
            if not existe:
                DaoCategoria.salvar(novaCategoria)
                print('categoria cadastrada com sucesso')
            else:
                print(' a categoria que deseja cadastrar ja existe')



    def removercategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        if len(cat) <= 0:
            print('a categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].Categoria == categoriaRemover:
                    del x[i]
                    break
            print('categoria removida com sucesso')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines('\n')

# a = ControllerCategoria()
# # a.cadastracategoria('legumes')
# a.removercategoria('legumes')

    def alterarcategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria ==  categoriaAlterada, x))

            if len(cat1) == 0:

                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x ))
                print('a categoria foi alterada com sucesso')
            else:
                print('a categoria ja existe')

        else:
            print('a categoria que deseja alterar nao existe')


        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

# a = ControllerCategoria()
# a.alterarcategoria('ale', 'Frutas')
    