#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TESTE - DETECÇÃO AUTOMÁTICA DE NEGÓCIOS
Valida se o sistema detecta corretamente diferentes tipos de negócio
"""

def teste_deteccao_negocios():
    print("\n" + "="*60)
    print("🧪 TESTE - DETECÇÃO AUTOMÁTICA DE NEGÓCIOS")
    print("="*60)
    
    # Casos de teste
    casos_teste = [
        # ADVOCACIA
        {"input": "no meu caso é advogacia", "esperado": "advogado"},
        {"input": "sou advogado", "esperado": "advogado"},
        {"input": "trabalho com direito", "esperado": "advogado"},
        {"input": "escritório jurídico", "esperado": "advogado"},
        
        # RESTAURANTE
        {"input": "tenho uma pizzaria", "esperado": "restaurante"},
        {"input": "trabalho com delivery", "esperado": "restaurante"},
        {"input": "restaurante italiano", "esperado": "restaurante"},
        {"input": "vendo comida", "esperado": "restaurante"},
        
        # CLÍNICA
        {"input": "sou médico", "esperado": "clínica"},
        {"input": "tenho uma clínica", "esperado": "clínica"},
        {"input": "consultório odontológico", "esperado": "clínica"},
        
        # SALÃO
        {"input": "trabalho com cabelo", "esperado": "salão"},
        {"input": "salão de beleza", "esperado": "salão"},
        {"input": "faço manicure", "esperado": "salão"},
        
        # LOJA
        {"input": "vendo roupas", "esperado": "loja"},
        {"input": "tenho uma loja", "esperado": "loja"},
        
        # CASOS SEM DETECÇÃO
        {"input": "oi", "esperado": None},
        {"input": "como funciona?", "esperado": None},
    ]
    
    acertos = 0
    total = len(casos_teste)
    
    print("🔍 EXECUTANDO CASOS DE TESTE:")
    print("-" * 60)
    
    for i, caso in enumerate(casos_teste, 1):
        input_text = caso["input"]
        esperado = caso["esperado"]
        
        # Simular detecção (lógica igual ao código)
        detectado = simular_deteccao(input_text)
        
        status = "✅" if detectado == esperado else "❌"
        print(f"{i:2d}. {status} '{input_text}'")
        print(f"    → Esperado: {esperado}")
        print(f"    → Detectado: {detectado}")
        
        if detectado == esperado:
            acertos += 1
        print()
    
    # Relatório final
    percentual = (acertos / total) * 100
    print("="*60)
    print("📊 RESULTADO FINAL:")
    print(f"✅ Acertos: {acertos}/{total} ({percentual:.1f}%)")
    print(f"❌ Erros: {total - acertos}")
    
    if percentual >= 90:
        print("\n🎉 EXCELENTE! Sistema detectando corretamente!")
    elif percentual >= 70:
        print("\n👍 BOM! Maioria dos casos funcionando.")
    else:
        print("\n⚠️ PRECISA MELHORAR! Muitos casos falhando.")
    
    # Mostrar configurações que serão aplicadas
    print("\n🎯 CONFIGURAÇÕES AUTOMÁTICAS:")
    print("-" * 60)
    
    exemplos_config = {
        "advogado": {
            "nome": "Escritório de Advocacia",
            "reservas": "✅ Sim (consultas)",
            "delivery": "❌ Não",
            "horario": "Seg-Sex: 8h-18h",
            "servicos": "Direito Civil, Trabalhista, Empresarial"
        },
        "restaurante": {
            "nome": "Restaurante Profissional", 
            "reservas": "✅ Sim (mesas)",
            "delivery": "✅ Sim",
            "horario": "Seg-Dom: 11h-23h",
            "servicos": "Pratos executivos, pizzas, lanches"
        },
        "clínica": {
            "nome": "Clínica Profissional",
            "reservas": "✅ Sim (consultas)", 
            "delivery": "❌ Não",
            "horario": "Seg-Sex: 7h-19h",
            "servicos": "Consultas médicas, exames"
        }
    }
    
    for tipo, config in exemplos_config.items():
        print(f"\n📋 {tipo.upper()}:")
        for campo, valor in config.items():
            print(f"   • {campo}: {valor}")
    
    print("\n" + "="*60)

def simular_deteccao(message):
    """Simula a lógica de detecção do sistema"""
    msg = message.lower()
    
    business_keywords = {
        'advogado': ['advogado', 'advogada', 'advocacia', 'direito', 'juridico', 'jurídico', 'lei', 'processo', 'tribunal', 'contrato'],
        'restaurante': ['restaurante', 'pizza', 'pizzaria', 'comida', 'lanche', 'lanchonete', 'bar', 'café', 'cardápio', 'delivery'],
        'loja': ['loja', 'venda', 'produtos', 'roupas', 'calçados', 'acessórios', 'varejo', 'mercado', 'shopping'],
        'clínica': ['clínica', 'médico', 'médica', 'saúde', 'consulta', 'exame', 'hospital', 'tratamento', 'consultório'],
        'salão': ['salão', 'cabelo', 'beleza', 'estética', 'manicure', 'pedicure', 'corte', 'penteado', 'barbearia'],
        'oficina': ['oficina', 'mecânica', 'carro', 'auto', 'conserto', 'manutenção', 'peças', 'motor'],
        'hotel': ['hotel', 'pousada', 'hospedagem', 'quarto', 'reserva', 'turismo', 'viagem'],
        'farmácia': ['farmácia', 'remédio', 'medicamento', 'droga', 'receita', 'saúde', 'manipulação']
    }
    
    for tipo, keywords in business_keywords.items():
        if any(keyword in msg for keyword in keywords):
            return tipo
    
    return None

if __name__ == "__main__":
    teste_deteccao_negocios() 