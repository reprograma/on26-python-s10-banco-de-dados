import sqlite3
import csv

# Abaixo as funções extras
# edição
def data_update(banco, tabela, id_registro, novo_valor, campo):
    connection = sqlite3.connect(f'{banco}.db')
    cursor = connection.cursor()
    atualizar_conteudo = f"UPDATE {tabela} SET {campo} = ? WHERE id = ?"
    cursor.execute(atualizar_conteudo, (novo_valor, id_registro))
    connection.commit()
    connection.close()

# deleção
def delete_register(banco, tabela, id_registro):
    connection = sqlite3.connect(f'{banco}.db')
    cursor = connection.cursor()
    excluir_conteudo = f"DELETE FROM {tabela} WHERE id = ?"
    cursor.execute(excluir_conteudo, (id_registro,))
    connection.commit()
    connection.close()


# chamando as funções para atualizar os dados.
data_update("health_indicators", "pharmaceuticals",4,"newAustralia","Country")
data_update("maternal_mortality", "maternal_mortality",2,"newAfeghanistan","Entity")

delete_register("health_indicators", "pharmaceuticals",3)
delete_register("maternal_mortality", "maternal_mortality",4)


