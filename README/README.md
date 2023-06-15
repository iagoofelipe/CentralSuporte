# Central Suporte
Automatizando processos realizados durante o dia a dia

# Conteudos

- [Uso](#)
    - [Flags](#Flags)
        - `--w`
        - `--s`
- [Atendimentos](#Atendimentos)


# Observações relevantes
As configurções armazenadas em ``settings.json`` são adicionadas ao Registros do Windows, desta forma, é ideal utilizar a flag ``-update`` para realizar alterações simultâneas, como pastas padrão e dentre outros



## Flags
As flags só estão disponíveis com o código fonte ``.py``, versões de ``.exe`` não possuem.

``` powershell
python CentralSuporte.py comando <opcoes> <valores>
```

# Atendimentos

[(retornar ao topo)](#) 

Utilizado para categorizar e contabilizar os atendimentos realizados no dia a dia.

- ### Arquivos obrigatórios no diretório padrão:
    - ``credentials.json``
    - ``tipos_de_atendimentos.json``