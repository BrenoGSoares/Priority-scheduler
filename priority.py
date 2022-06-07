#Transforma o arquivo em uma lista
def ler_arq(x):
  arq = open(x, 'r')
  lista = arq.readlines()
  new_lista =[]
  for linha in lista:
    linha = linha.rstrip('\n')
    new_lista.append(linha)
  arq = arq.close()
  return new_lista

#Encontra o tipo da lista
def type_alg():
  list_of_process = ler_arq('prioridades.txt')
  type_my_alg = list_of_process[0]
  selection = type_my_alg.split("|")
  return selection

#lista de listas
def list_of_list():
  arq = ler_arq('prioridades.txt')
  arq.pop(0)
  new_list =[]
  tam = len(arq)
  for i in range(tam):
    new_list.append([arq[i]])
  arq = []
  for i in range(tam):
    aux = new_list[i]
    aux_1 = aux[0]
    arq.append(aux_1.split("|"))
  return arq

#organizando por prioridade e por menor tempo
def org_priority():
  my_list = list_of_list()
  my_list_sorted = sorted(my_list, key = lambda x:(x[3], x[2]))
  return my_list_sorted

def temp():
  pass

def repre(i):
  list_priority = org_priority()
  element_list = list_priority[i]
  print('Process Number: ' + element_list[0] + ' ID Process: ' + element_list[1])

#função principal
def main():
  alg_esc = type_alg()
  if (alg_esc[0] == 'prioridade'):
    period = alg_esc[1]
    priority_list = org_priority()
    for i in range(len(priority_list)):
      repre(i)

  

main()
