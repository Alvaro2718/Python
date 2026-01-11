import random
import copy

MENSAJE_ERROR = "elige una opción válida"
VIDAS_MAX = 5

# Daños base de la espada
DANIOS_BASE = {"1": 6, "2": 9, "3": 16}
# Daños con espada mejorada
DANIOS_MEJORADA = {"1": 8, "2": 12, "3": 20}
FALLO_ESPECIAL = 0.35  # 35%


def pedir_opcion(mensaje, opciones_validas):
    """Pide una opción y no deja avanzar hasta que sea válida."""
    while True:
        op = input(mensaje).strip()
        if op in opciones_validas:
            return op
        print(MENSAJE_ERROR)


def irse_a_casa(nombre):
    print(f"\n{nombre} se va a casa por cagao.")


def clamp_vidas(vidas):
    return max(0, min(VIDAS_MAX, vidas))


def nuevo_inventario():
    return {"espada": False, "espada_mejorada": False, "llave": False, "comida": False, "manzana": False}


def elegir_ataque():
    print("\nElige tu ataque con la espada ⚔️")
    print("1) Corte ligero (poco efectivo, pero seguro)")
    print("2) Tajo Doble (ataque medio)")
    print("3) FATALITY (35% de fallar)")
    return pedir_opcion("Opción (1/2/3): ", ["1", "2", "3"])


def calcular_danio(ataque, inventario):
    """Devuelve (danio, fallo_bool)."""
    tabla = DANIOS_MEJORADA if inventario["espada_mejorada"] else DANIOS_BASE

    if ataque in ("1", "2"):
        return tabla[ataque], False

    # Especial
    if random.random() < FALLO_ESPECIAL:
        return 0, True
    return tabla["3"], False


def combatir(nombre, enemigo, vida_enemigo, vidas, inventario):
    """
    Combate por turnos:
    - Requiere espada.
    - Cada turno el jugador ataca, luego el enemigo responde (si sigue vivo).
    - El enemigo quita 1 vida por turno.
    Devuelve (vidas, victoria_bool).
    """
    if not inventario["espada"]:
        print(f"\nNo tienes espada para luchar contra {enemigo}.")
        return vidas, False

    print(f"\n⚔️ ¡COMBATE! Te enfrentas a: {enemigo}")
    while vida_enemigo > 0 and vidas > 0:
        print(
            f"\n👤 {nombre} | ❤️ Vidas: {vidas} | 🧟 {enemigo} vida: {vida_enemigo}")

        ataque = elegir_ataque()
        danio, fallo = calcular_danio(ataque, inventario)

        if fallo:
            print("❌ El ataque especial falló y te quedas vendido")
        else:
            print(f"✅ Golpeas y haces {danio} de daño")

        vida_enemigo -= danio

        if vida_enemigo <= 0:
            print(f"\n💥 ¡Has derrotado a {enemigo}!")
            return vidas, True

        # Turno enemigo
        print(f"👹 {enemigo} contraataca... ¡pierdes 1 vida!")
        vidas -= 1

    return vidas, False


def duelo_ppt(vidas):
    """
    Piedra/Papel/Tijera:
    - 3 intentos por duelo.
    - Si pierdes los 3 intentos del duelo => pierdes 1 vida.
    - Debes ganar al menos una ronda para superar al guardián.
    Devuelve vidas actualizadas y si superó el duelo.
    """
    opciones = {"1": "piedra", "2": "papel", "3": "tijeras"}
    gana_a = {"piedra": "tijeras", "tijeras": "papel", "papel": "piedra"}

    print("\n👁️ El Guardián de la Cripta te reta a Piedra, Papel o Tijera.")
    print("Debes ganarle para continuar. Tienes 3 intentos.")

    intentos = 3
    while intentos > 0:
        print("\n1) Piedra\n2) Papel\n3) Tijeras")
        elec = pedir_opcion("Elige (1/2/3): ", ["1", "2", "3"])
        jugador = opciones[elec]
        guard = random.choice(list(opciones.values()))

        print(f"Tú: {jugador} | Guardián: {guard}")

        if jugador == guard:
            print("🤝 Empate. Repite.")
        elif gana_a[jugador] == guard:
            print("✅ ¡Ganas el duelo! El Guardián te deja pasar.")
            return vidas, True
        else:
            intentos -= 1
            print(f"❌ Pierdes esta ronda. Intentos restantes: {intentos}")

    # Si llega aquí: perdió los 3 intentos
    vidas -= 1
    print("\n👁️ El Guardián se ríe... Pierdes 1 vida por fallar el duelo.")
    return vidas, False


# ---------------------- SECCIONES DE HISTORIA ----------------------

def intro_mision(nombre):
    print("\nEl rey te encomienda una misión que nadie quiere aceptar.")
    print("“Debes rescatar a la princesa raptada por una banda de malhechores.”")
    print("Dicen que la tienen en una cueva... y que la cueva está encantada.")

    print("\n1) Aceptar misión")
    print("2) Irte a casa")
    op = pedir_opcion("Elige (1/2): ", ["1", "2"])
    if op == "2":
        irse_a_casa(nombre)
        return False
    return True


def camino_hasta_bosque(nombre, vidas=VIDAS_MAX):
    print("\nCOMIENZA LA AVENTURA")
    print(f"\n👤 {nombre} | ❤️ Vidas: {vidas}")
    print("\nSales del castillo. Tienes un largo camino por delante hasta llegar al bosque.")
    print("1) Avanzar")
    print("2) Volver a casa")
    op = pedir_opcion("Elige (1/2): ", ["1", "2"])
    if op == "2":
        irse_a_casa(nombre)
        return False
    return True


def encuentro_bosque(nombre, vidas, inventario):
    print("\nLlegas al bosque y encuentras dos caminos:")
    print("1) Izquierda (un caballero bloquea el paso)")
    print("2) Derecha (campesinos con problemas para cruzar el río)")

    op = pedir_opcion("Elige (1/2): ", ["1", "2"])

    if op == "1":
        print("\n🛡️ Un caballero no te deja cruzar. Te obliga a pelear.")
        print("La batalla es dura... pierdes 2 vidas, pero consigues una espada.")
        vidas -= 2
        vidas = clamp_vidas(vidas)
        inventario["espada"] = True
        return vidas, True  # cruzó el río al final

    # Camino derecha
    print("\nVes a un grupo de campesinos intentando cruzar el río.")
    print("1) Ayudar a campesinos")
    print("2) Pasar de largo")

    op2 = pedir_opcion("Elige (1/2): ", ["1", "2"])
    if op2 == "1":
        print("\nLos ayudas a cruzar. Te dan un poco de COMIDA como agradecimiento.")
        inventario["comida"] = True
        print("Entre todos, cruzáis el río con éxito.")
        return vidas, True
    else:
        print("\nIntentas cruzar por tu cuenta... la corriente te arrastra.")
        print("💀 Te ahogas en el río.")
        vidas = 0
        return vidas, False


def encuentro_ogro(nombre, vidas, inventario):
    print("\nTras cruzar el río, un OGRO te bloquea el paso.")

    if inventario["espada"]:
        print("Tienes espada: tendrás que luchar.")
        vidas, gano = combatir(nombre, "Ogro", 17, vidas, inventario)
        if not gano:
            return vidas, False
        print("🔑 Al caer el ogro, consigues una LLAVE.")
        inventario["llave"] = True
        return vidas, True

    if inventario["comida"]:
        print("Tienes comida: la usas para distraer al ogro y pasar sin pelear.")
        print("🔑 Mientras el ogro se distrae, consigues una LLAVE.")
        inventario["llave"] = True
        return vidas, True

    # Por diseño, siempre deberías tener espada o comida, pero por seguridad:
    print("No tienes ni espada ni comida... el ogro te aplasta.")
    vidas = 0
    return vidas, False


def decision_seguir_o_casa(nombre):
    print("\nDespués de conseguir la llave:")
    print("1) Continuar atravesando el bosque")
    print("2) Volver a casa")
    op = pedir_opcion("Elige (1/2): ", ["1", "2"])
    if op == "2":
        irse_a_casa(nombre)
        return False
    return True


def tronco(nombre, vidas, inventario):
    print("\nEl camino está cortado por un gran tronco.")
    print("1) Cortar tronco")
    print("2) Esquivar el tronco")

    op = pedir_opcion("Elige (1/2): ", ["1", "2"])

    if op == "1":
        if inventario["espada"]:
            print("\nCortas el tronco con tu espada y sigues adelante.")
            return vidas, True
        print("\nNo tienes espada. No puedes cortar el tronco.")
        print("Debes elegir esquivar para continuar.")
        # obligamos a esquivar
        print("Esquivas el tronco como puedes... y te haces daño: -2 vidas.")
        vidas -= 2
        return clamp_vidas(vidas), True

    # Esquivar
    if not inventario["espada"]:
        print("\nSaltas/esquivas el tronco sin espada... te golpeas: -2 vidas.")
        vidas -= 2
        return clamp_vidas(vidas), True

    print("\nCon espada podrías cortarlo, pero decides esquivar igualmente.")
    print("Lo logras sin problemas.")
    return vidas, True


def manzano(vidas, inventario):
    print("\nLlegas a un claro perfecto para descansar y ves un manzano:")
    print("1) Recolectar manzanas (obtienes MANZANA y recuperas 2 vidas)")
    print("2) No recolectar")

    op = pedir_opcion("Elige (1/2): ", ["1", "2"])
    if op == "1":
        inventario["manzana"] = True
        vidas = clamp_vidas(vidas + 2)
        print("\nRecolectas una MANZANA 🍎 y te sientes mejor (+2 vidas).")
    else:
        print("\nDecides no recolectar nada.")
    return vidas


def mercader(nombre, vidas, inventario):
    print("\nEn el camino te encuentras con un mercader.")
    print(f"\n👤 {nombre} | ❤️ Vidas: {vidas}")
    if not inventario["manzana"]:
        print("El mercader mira tu bolsa... No tienes MANZANA para comerciar.")
        print("El mercader se despide y sigue su camino.")
        return vidas

    print("Puedes comerciar con tu MANZANA 🍎. El mercader te ofrece:")
    print("1) Recuperar toda la vida (vuelves a 5 vidas)")
    print("2) Comprar espada (solo si no tienes)")
    print("3) Mejorar espada (doble mejora: 8/12/20)")

    op = pedir_opcion("Elige (1/2/3): ", ["1", "2", "3"])

    if op == "1":
        print("\nLe das la MANZANA. El mercader te cura por completo.")
        inventario["manzana"] = False
        vidas = VIDAS_MAX

    elif op == "2":
        if inventario["espada"]:
            print("\nEl mercader se ríe: “ya tienes espada en tu inventario”.")
        else:
            print("\nCambias la MANZANA por una espada ⚔️.")
            inventario["manzana"] = False
            inventario["espada"] = True

    else:  # op == "3"
        if not inventario["espada"]:
            print("\nNo puedes mejorar una espada que no tienes.")
        elif inventario["espada_mejorada"]:
            print("\nTu espada ya está mejorada.")
        else:
            print("\nCambias la MANZANA por una mejora de espada. Ahora hace más daño.")
            inventario["manzana"] = False
            inventario["espada_mejorada"] = True

    print("\nEl mercader se despide: “¡Buena suerte en la cueva!”")
    return vidas


def preguntar_guardado():
    print("\n¿Deseas guardar partida?")
    print("1) Sí")
    print("2) No")
    op = pedir_opcion("Elige (1/2): ", ["1", "2"])
    return op == "1"


def entrada_cueva(nombre, inventario):
    print("\nSigues atravesando el bosque...")
    print("Encuentras la entrada a una cueva con una puerta de piedra y una cerradura.")
    print("1) Usar llave")

    pedir_opcion("Elige (1): ", ["1"])

    if inventario["llave"]:
        print("\nLa puerta se abre.")
        return True

    # Por seguridad (aunque dijiste que siempre la tendrá)
    print("\nNo tienes la llave... no puedes entrar.")
    return False


def enemigo_caminos(nombre, vidas, inventario):
    print("\nEn el interior de la cueva aparecen 2 caminos. ¿Cuál quieres tomar?")
    print("1) Izquierda")
    print("2) Derecha")
    op = pedir_opcion("Elige (1/2): ", ["1", "2"])

    print("\nAl recorrer el camino te encuentras con un enemigo...")

    if op == "1":
        enemigo = "Murciélagos"
    else:
        enemigo = "Cocodrilo"

    # Para esta parte damos por hecho que ya puede tener espada (por compra o por caballero).
    # Si llegara sin espada, no podría avanzar: perdería.
    vidas, gano = combatir(nombre, enemigo, 20, vidas, inventario)
    if not gano:
        return vidas, False

    print("\n✨ Al derrotar al enemigo, encuentras un objeto curativo.")
    vidas = VIDAS_MAX
    print("Recuperas toda la vida (5).")
    return vidas, True


def guardian_cripta(vidas):
    print("\nLlegas a una sala. En el centro aparece “El Guardián de la Cripta”.")
    print("Te amenaza y exige un duelo para dejarte pasar.")
    print("1) Aceptar combate")

    pedir_opcion("Elige (1): ", ["1"])

    superado = False
    while vidas > 0 and not superado:
        vidas, superado = duelo_ppt(vidas)
        if not superado and vidas > 0:
            print("\nEl Guardián: “Puedes intentarlo de nuevo...”")
    return vidas, superado


def dragon_final(nombre, vidas, inventario):
    print("\nLlegas a las mazmorras. Ahí debe estar la princesa...")
    print("Pero un DRAGÓN custodia la entrada.")
    vidas, gano = combatir(nombre, "Dragón", 30, vidas, inventario)
    if not gano:
        return vidas, False

    print("\n👑 ¡Has derrotado al Dragón!")
    print("Encuentras a la princesa y la rescatas. ¡MISIÓN CUMPLIDA!")
    return vidas, True


# ---------------------- LOOP PRINCIPAL CON REINICIO Y CHECKPOINT ----------------------

def partida_completa(nombre, checkpoint):
    """
    Ejecuta una partida desde el inicio (o desde checkpoint si se aplica en carga).
    Devuelve: (estado, checkpoint)
    estado: "victoria" | "salir" | "muerto"
    checkpoint: dict con {"existe": bool, "vidas": int, "inventario": dict, "fase": str}
    """
    vidas = VIDAS_MAX
    inventario = nuevo_inventario()

    # --- Intro ---
    if not intro_mision(nombre):
        return "salir", checkpoint

    if not camino_hasta_bosque(nombre):
        return "salir", checkpoint

    # --- Bosque y río ---
    vidas, cruzo = encuentro_bosque(nombre, vidas, inventario)
    if vidas <= 0:
        return "muerto", checkpoint

    if not cruzo:
        return "muerto", checkpoint

    # --- Ogro y llave ---
    vidas, ok = encuentro_ogro(nombre, vidas, inventario)
    if vidas <= 0 or not ok:
        return "muerto", checkpoint

    # --- Decisión seguir o casa ---
    if not decision_seguir_o_casa(nombre):
        return "salir", checkpoint

    # --- Tronco ---
    vidas, _ = tronco(nombre, vidas, inventario)
    if vidas <= 0:
        return "muerto", checkpoint

    # --- Avanzar o casa ---
    print("\nSigues atravesando el bosque:")
    print("1) Avanzar")
    print("2) Volver a casa")
    op = pedir_opcion("Elige (1/2): ", ["1", "2"])
    if op == "2":
        irse_a_casa(nombre)
        return "salir", checkpoint

    # --- Manzano ---
    vidas = manzano(vidas, inventario)
    if vidas <= 0:
        return "muerto", checkpoint

    # --- Mercader ---
    vidas = mercader(nombre, vidas, inventario)
    if vidas <= 0:
        return "muerto", checkpoint

    # --- Preguntar guardado (checkpoint) ---
    if preguntar_guardado():
        checkpoint["existe"] = True
        checkpoint["vidas"] = vidas
        checkpoint["inventario"] = copy.deepcopy(inventario)
        checkpoint["fase"] = "entrada_cueva"
        print("✅ Partida guardada.")
    else:
        print("No guardas partida.")

    # --- Continuar o casa ---
    print("\n¿Continuar?")
    print("1) Continuar")
    print("2) Volver a casa")
    op = pedir_opcion("Elige (1/2): ", ["1", "2"])
    if op == "2":
        irse_a_casa(nombre)
        return "salir", checkpoint

    # --- Entrada cueva ---
    if not entrada_cueva(nombre, inventario):
        return "muerto", checkpoint

    # --- Enemigo por camino (murciélagos / cocodrilo) ---
    vidas, ok = enemigo_caminos(nombre, vidas, inventario)
    if vidas <= 0 or not ok:
        return "muerto", checkpoint

    # --- Seguir avanzando ---
    print("\n¿Seguir avanzando?")
    print("1) Seguir avanzando por la cueva")
    pedir_opcion("Elige (1): ", ["1"])

    # --- Avanzar ---
    print("\nAvanzas por la cueva...")
    print("1) Avanzar")
    pedir_opcion("Elige (1): ", ["1"])

    # --- Avanzar sin evento ---
    print("\nSigues tu camino. La cueva parece no tener fin...")
    print("1) Avanzar")
    pedir_opcion("Elige (1): ", ["1"])

    # --- Guardián PPT ---
    vidas, superado = guardian_cripta(vidas)
    if vidas <= 0 or not superado:
        return "muerto", checkpoint

    # --- Continuar ---
    print("\nAtraviesas la plaza central de la cueva y continúas.")
    print("1) Avanzar")
    pedir_opcion("Elige (1): ", ["1"])

    # --- Dragón final ---
    vidas, victoria = dragon_final(nombre, vidas, inventario)
    if vidas <= 0 or not victoria:
        return "muerto", checkpoint

    return "victoria", checkpoint


def cargar_checkpoint(checkpoint):
    """
    Devuelve (vidas, inventario, fase) del checkpoint.
    """
    return checkpoint["vidas"], copy.deepcopy(checkpoint["inventario"]), checkpoint["fase"]


def run_desde_checkpoint(nombre, checkpoint):
    """
    Reanuda desde el checkpoint (entrada de cueva en adelante).
    Devuelve "victoria" | "salir" | "muerto"
    """
    vidas, inventario, fase = cargar_checkpoint(checkpoint)

    # En este diseño solo hay checkpoint en entrada_cueva.
    if fase != "entrada_cueva":
        return "muerto"

    print("\n✅ CARGANDO PARTIDA GUARDADA...")
    print(f"👤 {nombre} | ❤️ Vidas: {vidas}")
    print("Reanudas tu aventura justo antes de entrar en la cueva.")

    # Continuar o casa (por consistencia)
    print("\n¿Continuar?")
    print("1) Continuar")
    print("2) Volver a casa")
    op = pedir_opcion("Elige (1/2): ", ["1", "2"])
    if op == "2":
        irse_a_casa(nombre)
        return "salir"

    # Entrada cueva
    if not entrada_cueva(nombre, inventario):
        return "muerto"

    # Enemigo por camino
    vidas, ok = enemigo_caminos(nombre, vidas, inventario)
    if vidas <= 0 or not ok:
        return "muerto"

    # Seguir avanzando
    print("\n¿Seguir avanzando?")
    print("1) Seguir avanzando por la cueva")
    pedir_opcion("Elige (1): ", ["1"])

    # Avanzar
    print("\nAvanzas por la cueva...")
    print("1) Avanzar")
    pedir_opcion("Elige (1): ", ["1"])

    # Avanzar sin evento
    print("\nSigues tu camino. La cueva parece no tener fin...")
    print("1) Avanzar")
    pedir_opcion("Elige (1): ", ["1"])

    # Guardián PPT
    vidas, superado = guardian_cripta(vidas)
    if vidas <= 0 or not superado:
        return "muerto"

    # Continuar
    print("\nAtraviesas la plaza central de la cueva y continúas.")
    print("1) Avanzar")
    pedir_opcion("Elige (1): ", ["1"])

    # Dragón final
    vidas, victoria = dragon_final(nombre, vidas, inventario)
    if vidas <= 0 or not victoria:
        return "muerto"

    return "victoria"


def main():
    print("🎮 RESCATE EN LA CUEVA ENCANTADA")
    nombre = input("Introduce tu nombre: ").strip()
    if not nombre:
        nombre = "Jugador"

    checkpoint = {"existe": False, "vidas": VIDAS_MAX,
                  "inventario": nuevo_inventario(), "fase": ""}

    while True:
        estado, checkpoint = partida_completa(nombre, checkpoint)

        if estado == "victoria":
            print("\n🏆 ¡ENHORABUENA! Has completado el juego.")
            return

        if estado == "salir":
            print("\nHas salido del juego. ¡Hasta la próxima!")
            return

        # estado == "muerto"
        print("\n💀 GAME OVER 💀")
        print("Te has quedado sin vidas.")

        print("\n¿Volver a intentar o salir?")
        print("1) Volver a intentar")
        print("2) Salir")
        op = pedir_opcion("Elige (1/2): ", ["1", "2"])
        if op == "2":
            print("\nHas salido del juego. ¡Hasta la próxima!")
            return

        # Si hay checkpoint, ofrecer cargarlo
        if checkpoint["existe"]:
            print("\nTienes una partida guardada.")
            print("¿Deseas cargar la última partida guardada?")
            print("1) Sí")
            print("2) No (reinicio total)")
            op2 = pedir_opcion("Elige (1/2): ", ["1", "2"])

            if op2 == "1":
                resultado = run_desde_checkpoint(nombre, checkpoint)
                if resultado == "victoria":
                    print("\n🏆 ¡ENHORABUENA! Has completado el juego.")
                    return
                if resultado == "salir":
                    print("\nHas salido del juego. ¡Hasta la próxima!")
                    return

                # Si muere desde checkpoint, vuelve al bucle (pregunta otra vez)
                print("\n💀 GAME OVER 💀")
                continue

        # Reinicio total: simplemente el while repite y arranca partida_completa otra vez


if __name__ == "__main__":
    main()
