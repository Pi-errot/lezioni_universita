def toChar(variable):
    #return variable
    return "T" if variable else "F"

def format(variable, numOfTabs = 1):
    return toChar(variable) + numOfTabs *'\t'

print("Esercizio n.1: (a ↔ b) ∧ (c ↔ ¬a) → (b ↔ ¬a) ∧ (c → b)\n")
print("a\t b\t c\t a ↔ b\t c ↔ ¬a\t b ↔ ¬a\t c → b\t (c ↔ ¬a) → (b ↔ ¬a) \t\t (a ↔ b) ∧ (c ↔ ¬a) → (b ↔ ¬a) ∧ (c → b)")
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            AimplicatoB = a == b or b
            notA = not a
            CdoppiaImplicazioneAnegato = c == notA
            BdobbiaImplicazioneAnegato = b == notA
            CimplicatoB = c == b or b
            CdoppiaImplicazioneAnegato_implicato_BdobbiaImplicazioneAnegato = CdoppiaImplicazioneAnegato==BdobbiaImplicazioneAnegato or BdobbiaImplicazioneAnegato
            proposizione = AimplicatoB and CdoppiaImplicazioneAnegato_implicato_BdobbiaImplicazioneAnegato and CimplicatoB
            
            print(toChar(a), "\t", toChar(b), "\t", toChar(c), "\t", 
                  toChar(AimplicatoB), "\t", 
                  toChar(CdoppiaImplicazioneAnegato), "\t", 
                  toChar(BdobbiaImplicazioneAnegato), "\t", 
                  toChar(CimplicatoB), "\t", 
                  toChar(CdoppiaImplicazioneAnegato_implicato_BdobbiaImplicazioneAnegato), "\t\t\t\t", 
                  toChar(CdoppiaImplicazioneAnegato_implicato_BdobbiaImplicazioneAnegato)
                  )


print("Esercizio n.2: (a ∧ b) → (a ∨ ¬c) ∧ (c ∨ ¬b)\n")
print("a\t b\t c\t (a ∧ b)\t (a ∨ ¬c)\t (c ∨ ¬b)\t (a ∨ ¬c) ∧ (c ∨ ¬b)\t (a ∧ b) → (a ∨ ¬c) ∧ (c ∨ ¬b)\n")
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            AandB = a and b
            aorNotC = a or (not c)
            corNotB = c or (not b)
            AorNotC_and_CorNotB = aorNotC and corNotB
            proposizione = AandB == AorNotC_and_CorNotB or AorNotC_and_CorNotB
            print(format(a),format(b),format(c),
                  format(AandB,2),
                  format(aorNotC,2),
                  format(corNotB,2),
                  format(AorNotC_and_CorNotB,3),
                  format(proposizione)
                  )

print("Esercizio n.3: (a ∨ c) → (¬a ∧ ¬b) ∨ (¬b ∨ c)\n")
print("a\t b\t c\t (a ∨ c)\t (¬a ∧ ¬b)\t (¬b ∨ c)\t (a ∨ c) → (¬a ∧ ¬b)\t\t (a ∨ c) → (¬a ∧ ¬b) ∨ (¬b ∨ c)\n")
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            AorC = a or c
            notAandNotB = (not (a or b)) #(not a) and (not b)
            notBorC = (not b) or c
            AorC_implicato_notAandNotB = AorC == notAandNotB or notAandNotB
            proposizione = AorC_implicato_notAandNotB or notBorC
            print(format(a),format(b),format(c),
                  format(AorC,2),
                  format(notAandNotB,2),
                  format(notBorC,2),
                  format(AorC_implicato_notAandNotB,4),
                  format(proposizione)
                  )         


print("Esercizio n.4: ((a ∧ ¬b) ↔ (¬a ∨ b)) → ((a ∧ ¬c) ∨ (¬a ∨ c) ∨ (c ↔ a) ∨ (b ∧ ¬a))\n")
print("a\t b\t c\t (a ∧ ¬b)\t (¬a ∨ b)\t (a ∧ ¬c)\t (¬a ∨ c)\t (c ↔ a)\t (b ∧ ¬a)\t (a ∧ ¬b) ↔ (¬a ∨ b)\t (a ∧ ¬c) ∨ (¬a ∨ c) ∨ (c ↔ a) ∨ (b ∧ ¬a)\t ((a ∧ ¬b) ↔ (¬a ∨ b)) → ((a ∧ ¬c) ∨ (¬a ∨ c) ∨ (c ↔ a) ∨ (b ∧ ¬a))\n")
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            AandNotB = a and (not b)
            notAorB = (not a) or b
            AandNotC = a and (not c)
            notAorC = (not a) or c
            CdoppiaImplicazioneA = c == a 
            bandNotA = b and (not a)
            
            AandNotB_doppiaImplicazione_notAorB = AandNotB == notAorB
            AandNotC_or_notAorC_or_CdoppiaImplicazioneA_or_bandNotA = AandNotC or notAorC or CdoppiaImplicazioneA or bandNotA
            proposizione = AandNotB_doppiaImplicazione_notAorB == AandNotC_or_notAorC_or_CdoppiaImplicazioneA_or_bandNotA or AandNotC_or_notAorC_or_CdoppiaImplicazioneA_or_bandNotA
            
            print(format(a),format(b),format(c),
                  format(AandNotB,2),
                  format(notAorB,2),
                  format(AandNotC,2),
                  format(notAorC,2),
                  format(CdoppiaImplicazioneA,2),
                  format(bandNotA,2),
                  format(AandNotB_doppiaImplicazione_notAorB,3),
                  format(AandNotC_or_notAorC_or_CdoppiaImplicazioneA_or_bandNotA,6),
                  format(proposizione)
                  )