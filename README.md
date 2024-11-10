# DIO-Bootcamp
Tradutor para documentos do Word (.docx)
Este script Python fornece funcionalidade para traduzir texto dentro de um documento do Word (.docx) para um idioma de destino especificado usando a API do Microsoft Translator.

Características
Traduz parágrafos individuais dentro de um documento do Word.
Salva o documento traduzido com um nome de arquivo anexado ao código do idioma de destino (por exemplo, "-pt-br.docx").
Requisitos
Python 3.x
requestsbiblioteca (instalar com pip install requests)
python-docxbiblioteca (instalar com pip install python-docx)
Uma assinatura do Azure Cognitive Services Translator (você precisará de uma chave de assinatura)
Uso
Obtenha uma chave de assinatura do Microsoft Translator:

Crie uma conta gratuita ou paga do Azure e provisione um recurso do Translator.
Acesse sua chave de assinatura no portal do Azure.
Código de atualização:

Substitua a subscription_keyvariável de espaço reservado pela sua chave de assinatura real.
Atualize a language_destinationvariável para o código do idioma de destino desejado (por exemplo, "pt-br" para português (Brasil)).
Execute o script:

Salve o código como um arquivo Python (por exemplo, translator.py).
Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute:
Batida
python translator.py
Use o código com cautela.

Este script espera que seu documento do Word esteja localizado no caminho especificado pela input_filevariável. Você pode modificar esta variável para apontar para o local real do seu documento.
Análise de funcionalidade
A translator_textfunção recebe texto e um idioma de destino como entradas e usa a API do Microsoft Translator para traduzir o texto.
A translate_documentfunção itera pelos parágrafos em um documento do Word, traduz cada parágrafo usando a translator_textfunção e salva o texto traduzido em um novo documento com o código do idioma de destino anexado ao nome do arquivo.
Notas adicionais
Este script não inclui tratamento de erros no momento. Considere implementar tratamento de erros para problemas potenciais como chaves de API inválidas, erros de rede ou problemas de acesso a arquivos.
O script atualmente imprime texto traduzido durante o processamento. Você pode querer modificá-lo para suprimir essa saída.
Este arquivo README fornece uma visão geral básica do seu código e sua funcionalidade. Sinta-se à vontade para personalizá-lo ainda mais com detalhes ou instruções adicionais, conforme necessário.
