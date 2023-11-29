import morph_kgc
config = """
             [FuentesCaninas_data_graph]
             mappings:papelerasCaninas.ttl

         """

g = morph_kgc.materialize(config)

