#Requisitos de bibliotecas
!pip install Unidecode

#Imports
import re
import string
from collections import Counter
import codecs
import unidecode

#
def words(text): return re.findall(r'\w+', text.lower())

#
def normalize(text): return unidecode.unidecode(text)

#Aprende com o texto de entrada

#Diretório
file_path = ''

#Arquivo
file = file_path + 'fernando-pessoa.txt'

#Abre o texto e carrega em memória
text_raw = codecs.open(file, 'r', 'iso-8859-1').read()

#Normaliza texto
text_normalized = normalize(text_raw)

#Separa texto em lista de palavras
words_in_text = words(text_normalized)

#Agrupa as palavras
WORDS = Counter(words_in_text)

#Cria todos os métodos para a utilização

#
def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    #print('\nP: ',(WORDS[word] / N))
    return WORDS[word] / N

#
def correction(word): 
    #import pdb; pdb.set_trace()
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

#
def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

#
def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    #print('\nknow: ',set(w for w in words if w in WORDS))
    return set(w for w in words if w in WORDS)

#
def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    #print ('\nedits1: ', set(deletes + transposes + replaces + inserts))
    return set(deletes + transposes + replaces + inserts)

#
def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

#
def corrections(phrase):
  final_text = ''
  normalized_text = normalize(phrase)
  normalized_text = normalized_text.lower()
  for word in normalized_text.split(' '):
    final_text = final_text + ' ' + correction(word)
  return final_text

#############################################################################################
#Teste
texto_errado = 'tacabaria jenelas mondo inacesiveu ambissoes istrada literaumente naviu'

print(texto_errado)
print(corrections(texto_errado).strip())
