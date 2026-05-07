import random
import asyncio


# asyncio permet de faire de la programmation concourante.
# Ce n'est pas à proprement dit du parallélisme, cela permet de définir des méthodes asynchrones.

# async: permet de déclarer une méthode comme asynchrone. Ceci retourne une coroutine (une méthode/fonction qui peut
# être suspendue, reprises
# await: suspends l'exécution de la coroutine dans laquelle await est contenue et redonne le contrôle à la boucle
# d'événement. Sera suspendue jusqu'à ce que l'appel suivant le await retourne
async def attendre_secondes(uid: int, secondes: float):
    print(f"{uid}: Va attendre {secondes} secondes")
    await asyncio.sleep(secondes)
    print(f"{uid} a terminé")


async def main():
    # asyncio.gather() permet de lancer plusieurs tâches asynchrones
    return await asyncio.gather(*(attendre_secondes(uid, random.randint(1, 10)) for uid in range(5)))


if __name__ == "__main__":
    # asyncio.run() cédule une coroutine pour exécution
    asyncio.run(main())
