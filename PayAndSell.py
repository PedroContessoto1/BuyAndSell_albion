from datetime import datetime
import sys

s_porc = lambda a, b: a * (1 - b * 0.01)

def help():
    print("python3 PayAndSell.py -n {numero de items} -c {preco de compra} -v {preco de venda}")
    print("Criar txt com as informacoes use (-s)")
    print("Colocar o nome do item use (-in)")

class PAS():
    PACK = 999

    def __init__(self, purchase_price, sale_price, num_item, name_item=None):
        self.purchase_price = float(purchase_price)
        self.sale_price = float(sale_price)
        self.num_item = float(num_item)
        self.name_item = name_item

    def intro(self):
        logo = ".------..------..------..------..------..------..------..------.\n" \
               "|P.--. ||A.--. ||S.--. ||J.--. ||O.--. ||K.--. ||E.--. ||R.--. |\n" \
               "| :/\: || (\/) || :/\: || :(): || :/\: || :/\: || (\/) || :(): |\n" \
               "| (__) || :\/: || :\/: || ()() || :\/: || :\/: || :\/: || ()() |\n" \
               "| '--'P|| '--'A|| '--'S|| '--'J|| '--'O|| '--'K|| '--'E|| '--'R|\n" \
               "`------'`------'`------'`------'`------'`------'`------'`------'\n"
        return logo

    def ruler(self):
        self.purchase_price = s_porc(self.purchase_price, 1.5)
        paid_value = self.num_item * self.purchase_price
        self.sale_price = s_porc(self.sale_price, 4.5)
        gross_profit = self.num_item * self.sale_price
        net_profit = gross_profit - paid_value
        return paid_value, gross_profit, net_profit

    def response(self):
        paid_value, gross_profit, net_profit = self.ruler()
        response = self.intro()
        response += "###################INPUT##################\n"
        response += f"Horario : {str(datetime.today())}\n"
        if self.name_item:
            response += f"Nome do item pesquisado : {self.name_item}\n"
        else:
            response += f"Nome do item pesquisado : None\n"
        response += f"Preço de compra : {self.purchase_price:.2f}\n"
        response += f"Preço de venda : {self.sale_price:.2f}\n"
        response += f"Numero de items : {self.num_item:.2f}\n"
        response += f"###################OUTPUT#################\n"
        response += f"Valor gasto : {paid_value:.2f}\n" \
                    f"Lucro bruto : {gross_profit:.2f}\n" \
                    f"lucro_liquido : {net_profit:.2f}\n" \
                    f"Imposto : {paid_value * 0.015:.2f}\n" \
                    f"##########################################"

        return response

    def create_txt(self):
        txt = open(f"Joker_search-{str(datetime.today()).replace(' ', '-').replace(':', '-')}.txt",
                   "w")
        response = self.response()
        for i in response:
            txt.writelines(i)
        txt.close()


def main():
    try:
        num_item = sys.argv[sys.argv.index("-n") + 1]
        purchase_price = sys.argv[sys.argv.index("-c") + 1]
        sale_price = sys.argv[sys.argv.index("-v") + 1]
        try:
            name_item = sys.argv[sys.argv.index("-in") + 1]
            pas = PAS(purchase_price, sale_price, num_item, name_item)
        except:
            pas = PAS(purchase_price, sale_price, num_item)
        if "-s" in sys.argv:
            pas.create_txt()
            print(pas.response())
        else:
            print(pas.response())
    except:
        help()


if __name__ == "__main__":
    main()
