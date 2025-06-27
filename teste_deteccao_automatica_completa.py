#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 TESTE COMPLETO - DETECÇÃO AUTOMÁTICA EXPANDIDA
Sistema de validação para todos os tipos de negócio do Brasil
"""

import json
from datetime import datetime

# Simulação da função de detecção (baseada no TypeScript)
def detect_business_type(message):
    """Detecta o tipo de negócio baseado em palavras-chave"""
    msg = message.lower()
    
    # Palavras-chave expandidas para todos os negócios brasileiros
    business_keywords = {
        # PROFISSIONAIS LIBERAIS
        'advogado': ['advogado', 'advogada', 'advocacia', 'direito', 'juridico', 'jurídico', 'lei', 'processo', 'tribunal', 'contrato', 'escritório jurídico', 'causas'],
        'contador': ['contador', 'contadora', 'contabilidade', 'contábil', 'imposto', 'declaração', 'fiscal', 'tributo'],
        'arquiteto': ['arquiteto', 'arquiteta', 'arquitetura', 'projeto', 'construção', 'planta', 'desenho'],
        'engenheiro': ['engenheiro', 'engenheira', 'engenharia', 'obra', 'construção', 'projeto'],
        'dentista': ['dentista', 'odonto', 'odontologia', 'dente', 'ortodontia', 'canal'],
        
        # SAÚDE E BEM-ESTAR
        'medico': ['médico', 'médica', 'medicina', 'clínica', 'consultório', 'saúde', 'consulta', 'exame', 'hospital', 'tratamento', 'pediatra', 'cardiologista'],
        'fisioterapeuta': ['fisioterapeuta', 'fisioterapia', 'reabilitação', 'fisio'],
        'psicologo': ['psicólogo', 'psicóloga', 'psicologia', 'terapia', 'psicoterapia'],
        'veterinario': ['veterinário', 'veterinária', 'pet', 'animal', 'cachorro', 'gato', 'petshop'],
        'farmacia': ['farmácia', 'remédio', 'medicamento', 'droga', 'receita', 'manipulação'],
        
        # ALIMENTAÇÃO
        'restaurante': ['restaurante', 'pizza', 'pizzaria', 'comida', 'lanche', 'lanchonete', 'bar', 'café', 'cardápio', 'delivery', 'ifood', 'uber eats', 'entrega'],
        'padaria': ['padaria', 'pão', 'pães', 'doce', 'bolo', 'confeitaria'],
        'acai': ['açaí', 'açai', 'vitamina', 'suco', 'smoothie'],
        'hamburgueria': ['hambúrguer', 'hamburgueria', 'burguer', 'lanches'],
        'churrascaria': ['churrascaria', 'churrasco', 'carne', 'rodízio'],
        
        # BELEZA E ESTÉTICA
        'salao': ['salão', 'cabelo', 'beleza', 'estética', 'manicure', 'pedicure', 'corte', 'penteado', 'barbearia', 'unha', 'cabeleireiro'],
        'estetica': ['estética', 'estético', 'laser', 'botox', 'preenchimento', 'harmonização'],
        'massagem': ['massagem', 'massagista', 'relaxante', 'terapêutica'],
        
        # VAREJO E COMÉRCIO
        'loja': ['loja', 'venda', 'produtos', 'varejo', 'shopping'],
        'roupas': ['roupas', 'moda', 'vestuário', 'calças', 'camisas', 'vestidos', 'fashion'],
        'calcados': ['calçados', 'sapatos', 'tênis', 'sandálias', 'chinelos'],
        'acessorios': ['acessórios', 'bolsas', 'relógios', 'joias', 'bijuterias'],
        'eletronicos': ['eletrônicos', 'celular', 'computador', 'tv', 'notebook', 'smartphone'],
        'mercado': ['mercado', 'supermercado', 'mercadinho', 'quitanda', 'hortifruti'],
        
        # SERVIÇOS AUTOMOTIVOS
        'oficina': ['oficina', 'mecânica', 'carro', 'auto', 'conserto', 'manutenção', 'peças', 'motor', 'freio'],
        'lavacao': ['lavação', 'lava-jato', 'lavagem', 'enceramento'],
        'borracharia': ['borracharia', 'pneu', 'pneus', 'calibragem'],
        
        # EDUCAÇÃO
        'escola': ['escola', 'colégio', 'educação', 'ensino', 'curso', 'aula', 'professor', 'professora'],
        'cursinho': ['cursinho', 'pré-vestibular', 'vestibular', 'enem'],
        'idiomas': ['idiomas', 'inglês', 'espanhol', 'francês', 'línguas'],
        
        # CASA E CONSTRUÇÃO
        'construcao': ['construção', 'pedreiro', 'obra', 'reforma', 'tijolo', 'cimento'],
        'pintura': ['pintura', 'pintor', 'tinta', 'parede'],
        'eletricista': ['eletricista', 'elétrica', 'energia', 'instalação'],
        'encanador': ['encanador', 'hidráulica', 'cano', 'vazamento', 'água'],
        'marcenaria': ['marcenaria', 'marceneiro', 'móveis', 'madeira', 'armário'],
        
        # TURISMO E HOSPEDAGEM
        'hotel': ['hotel', 'pousada', 'hospedagem', 'quarto', 'reserva', 'turismo', 'viagem'],
        'agencia': ['agência de viagens', 'turismo', 'pacotes', 'excursão'],
        
        # TRANSPORTE
        'taxi': ['taxi', 'táxi', 'uber', 'transporte', 'corrida'],
        'motoboy': ['motoboy', 'entrega', 'delivery', 'moto'],
        'caminhao': ['caminhão', 'frete', 'mudança', 'carga'],
        
        # EVENTOS E ENTRETENIMENTO
        'buffet': ['buffet', 'festa', 'evento', 'casamento', 'aniversário'],
        'musica': ['música', 'músico', 'banda', 'show', 'dj'],
        'fotografia': ['fotografia', 'fotógrafo', 'foto', 'casamento', 'book'],
        
        # TECNOLOGIA
        'informatica': ['informática', 'computador', 'técnico', 'software', 'hardware', 'TI'],
        'desenvolvedor': ['desenvolvedor', 'programador', 'site', 'app', 'sistema'],
        
        # AGRICULTURA E PECUÁRIA
        'agronegocio': ['agronegócio', 'fazenda', 'agricultura', 'pecuária', 'gado', 'plantação'],
        
        # SERVIÇOS DOMÉSTICOS
        'limpeza': ['limpeza', 'faxina', 'doméstica', 'diarista'],
        'lavanderia': ['lavanderia', 'lavagem', 'roupa', 'dry clean'],
        
        # ESPORTES E FITNESS
        'academia': ['academia', 'fitness', 'musculação', 'personal', 'ginástica'],
        'esportes': ['esportes', 'futebol', 'natação', 'tênis', 'vôlei'],
        
        # RELIGIOSO
        'igreja': ['igreja', 'pastor', 'religioso', 'casamento', 'batismo']
    }
    
    # Procurar correspondências
    for business_type, keywords in business_keywords.items():
        if any(keyword in msg for keyword in keywords):
            return business_type
    
    return None

def create_business_response(business_type):
    """Cria resposta personalizada para cada tipo de negócio"""
    responses = {
        'advogado': "Detectei que você trabalha com **advocacia**. Vou configurar seu funcionário IA especializado em atendimento jurídico.",
        'contador': "Detectei que você trabalha com **contabilidade**. Vou configurar seu funcionário IA especializado em serviços contábeis.",
        'medico': "Detectei que você trabalha com **medicina**. Vou configurar seu funcionário IA especializado em atendimento médico.",
        'dentista': "Detectei que você trabalha com **odontologia**. Vou configurar seu funcionário IA especializado em cuidados dentários.",
        'restaurante': "Detectei que você trabalha com **alimentação**. Vou configurar seu funcionário IA especializado em delivery e reservas.",
        'farmacia': "Detectei que você trabalha com **farmácia**. Vou configurar seu funcionário IA especializado em medicamentos e delivery.",
        'salao': "Detectei que você trabalha com **beleza**. Vou configurar seu funcionário IA especializado em agendamentos e cuidados estéticos.",
        'oficina': "Detectei que você trabalha com **serviços automotivos**. Vou configurar seu funcionário IA especializado em manutenção veicular.",
        'loja': "Detectei que você trabalha com **varejo**. Vou configurar seu funcionário IA especializado em vendas e atendimento comercial.",
        'hotel': "Detectei que você trabalha com **hospedagem**. Vou configurar seu funcionário IA especializado em reservas e turismo."
    }
    
    return responses.get(business_type, f"Detectei que você trabalha com **{business_type}**. Vou configurar seu funcionário IA especializado nesta área.")

def run_comprehensive_test():
    """Executa teste abrangente com 50+ casos de negócios brasileiros"""
    print("🚀 INICIANDO TESTE COMPLETO - DETECÇÃO AUTOMÁTICA EXPANDIDA")
    print("=" * 70)
    
    # Casos de teste expandidos - cobrindo todo o Brasil
    test_cases = [
        # PROFISSIONAIS LIBERAIS
        ("oi sou advogado", "advogado"),
        ("trabalho com advocacia", "advogado"),
        ("tenho um escritório jurídico", "advogado"),
        ("sou contador", "contador"),
        ("trabalho com contabilidade", "contador"),
        ("faço declaração de imposto", "contador"),
        ("sou arquiteto", "arquiteto"),
        ("trabalho com projetos", "arquiteto"),
        ("sou engenheiro civil", "engenheiro"),
        
        # SAÚDE
        ("sou médico", "medico"),
        ("tenho uma clínica", "medico"),
        ("sou dentista", "dentista"),
        ("trabalho com odontologia", "dentista"),
        ("sou fisioterapeuta", "fisioterapeuta"),
        ("trabalho com reabilitação", "fisioterapeuta"),
        ("sou psicólogo", "psicologo"),
        ("faço terapia", "psicologo"),
        ("sou veterinário", "veterinario"),
        ("cuido de pets", "veterinario"),
        ("tenho uma farmácia", "farmacia"),
        ("vendo medicamentos", "farmacia"),
        
        # ALIMENTAÇÃO
        ("tenho um restaurante", "restaurante"),
        ("trabalho com delivery", "restaurante"),
        ("tenho uma pizzaria", "restaurante"),
        ("trabalho com comida", "restaurante"),
        ("tenho uma padaria", "padaria"),
        ("vendo pães", "padaria"),
        ("trabalho com açaí", "acai"),
        ("vendo vitaminas", "acai"),
        ("tenho hamburgueria", "hamburgueria"),
        ("trabalho com lanches", "hamburgueria"),
        
        # BELEZA
        ("tenho um salão", "salao"),
        ("trabalho com cabelo", "salao"),
        ("sou cabeleireiro", "salao"),
        ("trabalho com estética", "estetica"),
        ("faço harmonização", "estetica"),
        ("trabalho com massagem", "massagem"),
        
        # VAREJO
        ("tenho uma loja", "loja"),
        ("trabalho com vendas", "loja"),
        ("vendo roupas", "roupas"),
        ("trabalho com moda", "roupas"),
        ("vendo calçados", "calcados"),
        ("trabalho com sapatos", "calcados"),
        ("tenho um mercado", "mercado"),
        ("trabalho com supermercado", "mercado"),
        
        # AUTOMOTIVO
        ("tenho uma oficina", "oficina"),
        ("trabalho com carros", "oficina"),
        ("faço conserto de auto", "oficina"),
        ("tenho lava-jato", "lavacao"),
        ("trabalho com lavagem", "lavacao"),
        ("tenho borracharia", "borracharia"),
        
        # EDUCAÇÃO
        ("tenho uma escola", "escola"),
        ("trabalho com educação", "escola"),
        ("dou aulas", "escola"),
        ("tenho cursinho", "cursinho"),
        ("trabalho com idiomas", "idiomas"),
        
        # CONSTRUÇÃO
        ("trabalho com construção", "construcao"),
        ("sou pedreiro", "construcao"),
        ("trabalho com pintura", "pintura"),
        ("sou eletricista", "eletricista"),
        ("sou encanador", "encanador"),
        ("trabalho com marcenaria", "marcenaria"),
        
        # TURISMO
        ("tenho um hotel", "hotel"),
        ("trabalho com hospedagem", "hotel"),
        ("tenho agência de viagens", "agencia"),
        
        # TRANSPORTE
        ("trabalho com taxi", "taxi"),
        ("sou motoboy", "motoboy"),
        ("trabalho com frete", "caminhao"),
        
        # EVENTOS
        ("trabalho com buffet", "buffet"),
        ("organizo festas", "buffet"),
        ("sou músico", "musica"),
        ("sou fotógrafo", "fotografia"),
        
        # TECNOLOGIA
        ("trabalho com informática", "informatica"),
        ("sou desenvolvedor", "desenvolvedor"),
        ("programo sistemas", "desenvolvedor"),
        
        # OUTROS
        ("trabalho com agronegócio", "agronegocio"),
        ("tenho fazenda", "agronegocio"),
        ("trabalho com limpeza", "limpeza"),
        ("tenho lavanderia", "lavanderia"),
        ("tenho academia", "academia"),
        ("trabalho com fitness", "academia"),
        ("tenho igreja", "igreja"),
        
        # CASOS QUE NÃO DEVEM DETECTAR
        ("oi", None),
        ("olá", None),
        ("bom dia", None),
        ("tudo bem?", None),
        ("preciso de ajuda", None)
    ]
    
    # Executar testes
    total_tests = len(test_cases)
    correct_detections = 0
    results = []
    
    for i, (message, expected) in enumerate(test_cases, 1):
        detected = detect_business_type(message)
        is_correct = detected == expected
        
        if is_correct:
            correct_detections += 1
            status = "✅ CORRETO"
        else:
            status = "❌ ERRO"
        
        result = {
            "test": i,
            "message": message,
            "expected": expected,
            "detected": detected,
            "correct": is_correct,
            "response": create_business_response(detected) if detected else "Perguntaria: Que tipo de estabelecimento você tem?"
        }
        
        results.append(result)
        
        print(f"{status} | Teste {i:2d}: '{message[:25]:25}' → {detected or 'None':15} | Esperado: {expected or 'None'}")
    
    # Estatísticas finais
    accuracy = (correct_detections / total_tests) * 100
    
    print("\n" + "=" * 70)
    print("📊 RELATÓRIO FINAL")
    print("=" * 70)
    print(f"✅ Testes corretos: {correct_detections}/{total_tests}")
    print(f"📈 Taxa de acerto: {accuracy:.1f}%")
    print(f"🎯 Meta de acerto: 95%")
    
    if accuracy >= 95:
        print("🏆 SUCESSO! Sistema aprovado para produção!")
    elif accuracy >= 90:
        print("⚠️  APROVADO com ressalvas. Considere ajustes nas palavras-chave.")
    else:
        print("❌ REPROVADO. Sistema precisa de melhorias significativas.")
    
    # Erros detalhados
    errors = [r for r in results if not r['correct']]
    if errors:
        print(f"\n🔍 ANÁLISE DE ERROS ({len(errors)} casos):")
        for error in errors[:10]:  # Mostrar até 10 erros
            print(f"   • '{error['message']}' → Detectou: {error['detected']}, Esperado: {error['expected']}")
    
    # Tipos de negócio detectados
    detected_types = [r['detected'] for r in results if r['detected']]
    unique_types = set(detected_types)
    
    print(f"\n🏪 TIPOS DE NEGÓCIO DETECTADOS ({len(unique_types)} diferentes):")
    for business_type in sorted(unique_types):
        count = detected_types.count(business_type)
        print(f"   • {business_type}: {count} detecções")
    
    # Salvar relatório
    report = {
        "timestamp": datetime.now().isoformat(),
        "total_tests": total_tests,
        "correct_detections": correct_detections,
        "accuracy": accuracy,
        "results": results,
        "detected_types": list(unique_types),
        "summary": {
            "status": "APROVADO" if accuracy >= 95 else "REPROVADO",
            "recommendation": "Pronto para produção" if accuracy >= 95 else "Precisa ajustes"
        }
    }
    
    with open('relatorio_deteccao_completa.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Relatório salvo: relatorio_deteccao_completa.json")
    return accuracy

if __name__ == "__main__":
    try:
        accuracy = run_comprehensive_test()
        exit(0 if accuracy >= 95 else 1)
    except Exception as e:
        print(f"❌ Erro durante teste: {e}")
        exit(1) 