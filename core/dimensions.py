"""
8 dimensiones y 24 comportamientos de la Rueda del Liderazgo Transformacional.
"""

DIMENSIONES = [
    {
        "id": 1,
        "nombre": "Visión e Inspiración",
        "fuente": "Motivación Inspiracional · Bass & Avolio",
        "color": "#FF6B4E",
        "icono": "🌟",
        "comportamientos": [
            {
                "id": "1.1",
                "descripcion": "Articulo una visión clara que orienta al equipo hacia el futuro",
                "orden": 1,
            },
            {
                "id": "1.2",
                "descripcion": "Genero entusiasmo y sentido de propósito en los demás",
                "orden": 9,
            },
            {
                "id": "1.3",
                "descripcion": "Conecto las metas individuales con la misión organizacional",
                "orden": 17,
            },
        ],
    },
    {
        "id": 2,
        "nombre": "Inteligencia Emocional",
        "fuente": "Autoconciencia, Empatía, Autorregulación · Goleman",
        "color": "#9b59b6",
        "icono": "🧠",
        "comportamientos": [
            {
                "id": "2.1",
                "descripcion": "Reconozco y gestiono mis propias emociones con madurez",
                "orden": 2,
            },
            {
                "id": "2.2",
                "descripcion": "Muestro empatía genuina hacia las personas de mi equipo",
                "orden": 10,
            },
            {
                "id": "2.3",
                "descripcion": "Mantengo la calma y ecuanimidad en situaciones de presión",
                "orden": 18,
            },
        ],
    },
    {
        "id": 3,
        "nombre": "Desarrollo de Personas",
        "fuente": "Consideración Individual · Bass & Avolio",
        "color": "#27ae60",
        "icono": "🌱",
        "comportamientos": [
            {
                "id": "3.1",
                "descripcion": "Identifico el potencial único de cada integrante del equipo",
                "orden": 3,
            },
            {
                "id": "3.2",
                "descripcion": "Delego con confianza para promover el crecimiento individual",
                "orden": 11,
            },
            {
                "id": "3.3",
                "descripcion": "Brindo retroalimentación oportuna, honesta y constructiva",
                "orden": 19,
            },
        ],
    },
    {
        "id": 4,
        "nombre": "Comunicación Transformadora",
        "fuente": "Enable Others to Act · Kouzes & Posner",
        "color": "#2980b9",
        "icono": "💬",
        "comportamientos": [
            {
                "id": "4.1",
                "descripcion": "Escucho activamente con presencia plena y sin juicios",
                "orden": 4,
            },
            {
                "id": "4.2",
                "descripcion": "Me comunico con claridad, autenticidad y poder de persuasión",
                "orden": 12,
            },
            {
                "id": "4.3",
                "descripcion": "Genero espacios de diálogo abierto y seguridad psicológica",
                "orden": 20,
            },
        ],
    },
    {
        "id": 5,
        "nombre": "Innovación y Pensamiento Crítico",
        "fuente": "Estimulación Intelectual · Bass & Avolio",
        "color": "#d4a017",
        "icono": "💡",
        "comportamientos": [
            {
                "id": "5.1",
                "descripcion": "Estimulo el cuestionamiento creativo del status quo",
                "orden": 5,
            },
            {
                "id": "5.2",
                "descripcion": "Fomento la experimentación y el aprendizaje del error",
                "orden": 13,
            },
            {
                "id": "5.3",
                "descripcion": "Tomo decisiones estratégicas integrando datos y visión",
                "orden": 21,
            },
        ],
    },
    {
        "id": 6,
        "nombre": "Cultura e Influencia Ética",
        "fuente": "Influencia Idealizada · Bass & Avolio",
        "color": "#1abc9c",
        "icono": "⚖️",
        "comportamientos": [
            {
                "id": "6.1",
                "descripcion": "Modelo con mis comportamientos los valores que promuevo",
                "orden": 6,
            },
            {
                "id": "6.2",
                "descripcion": "Construyo una cultura de confianza, respeto y colaboración",
                "orden": 14,
            },
            {
                "id": "6.3",
                "descripcion": "Ejerzo influencia basada en la integridad y la coherencia",
                "orden": 22,
            },
        ],
    },
    {
        "id": 7,
        "nombre": "Gestión del Cambio y Resiliencia",
        "fuente": "Liderazgo Adaptativo · Heifetz",
        "color": "#e67e22",
        "icono": "⚡",
        "comportamientos": [
            {
                "id": "7.1",
                "descripcion": "Lidero procesos de cambio con claridad y convicción",
                "orden": 7,
            },
            {
                "id": "7.2",
                "descripcion": "Gestiono la incertidumbre con agilidad y apertura mental",
                "orden": 15,
            },
            {
                "id": "7.3",
                "descripcion": "Involucro al equipo en la co-creación de nuevas soluciones",
                "orden": 23,
            },
        ],
    },
    {
        "id": 8,
        "nombre": "Propósito y Servicio",
        "fuente": "Servant Leadership · Greenleaf",
        "color": "#6c5ce7",
        "icono": "🤲",
        "comportamientos": [
            {
                "id": "8.1",
                "descripcion": "Actúo con coherencia entre mis valores personales y mi liderazgo",
                "orden": 8,
            },
            {
                "id": "8.2",
                "descripcion": "Pongo el bienestar y crecimiento del equipo como prioridad",
                "orden": 16,
            },
            {
                "id": "8.3",
                "descripcion": "Contribuyo activamente al impacto positivo en la organización y sociedad",
                "orden": 24,
            },
        ],
    },
]


def _enriquecer(dim, comp):
    return {
        "dim_id":     dim["id"],
        "dim_nombre": dim["nombre"],
        "dim_color":  dim["color"],
        "dim_icono":  dim["icono"],
        **comp,
    }


def get_comportamientos_formulario():
    """Orden para el formulario: intercalado por posición (1.1,2.1,...8.1, 1.2,...8.2, 1.3,...8.3)."""
    items = []
    for dim in DIMENSIONES:
        for comp in dim["comportamientos"]:
            items.append(_enriquecer(dim, comp))
    return sorted(items, key=lambda x: x["orden"])


def get_comportamientos_informe():
    """Mismo orden que el formulario."""
    return get_comportamientos_formulario()


def calcular_puntajes(respuestas: dict) -> dict:
    resultado = {}
    for dim in DIMENSIONES:
        scores  = []
        detalle = []
        for comp in dim["comportamientos"]:
            val = respuestas.get(comp["id"], 0)
            scores.append(val)
            detalle.append({"id": comp["id"], "descripcion": comp["descripcion"], "puntaje": val})
        promedio = round(sum(scores) / len(scores), 2) if scores else 0
        resultado[dim["id"]] = {
            "nombre":   dim["nombre"],
            "fuente":   dim["fuente"],
            "color":    dim["color"],
            "icono":    dim["icono"],
            "promedio": promedio,
            "detalle":  detalle,
        }
    return resultado
