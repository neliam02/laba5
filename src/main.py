import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.team import Team
from src.player import Player
from src.coach import Coach
from src.staff import Staff
from src.sponsor import Sponsor
from src.tournament import Tournament
from src.training_program import TrainingProgram


def main():
    # Створюємо команду
    team = Team("Dream Team")
    print(f"Створено команду: {team.name}")

    # Додаємо гравців
    player1 = Player("John Doe", "Advanced", ["Passing", "Shooting"])
    player2 = Player("Jane Doe", "Intermediate", ["Defense", "Dribbling"])
    team.recruitMember(player1)
    team.recruitMember(player2)

    # Додаємо тренера
    coach = Coach("Coach Mike", 15, "Strategy")
    team.recruitMember(coach)

    # Додаємо персонал
    analyst = Staff("Alice Smith", 5, "Analyst")
    team.recruitMember(analyst)

    # Додаємо спонсора
    sponsor = Sponsor("Tech Corp", 5000)
    print(f"Спонсор {sponsor.name} підтримує команду з бюджетом {sponsor.budget}.")

    # Додаємо турнір
    tournament = Tournament("Championship", 10000)
    print(f"Команда бере участь у турнірі: {tournament.name} з призовим фондом {tournament.prize_pool}.")

    # Додаємо тренувальну програму
    training_program = TrainingProgram("Strength Training", "4 weeks")
    print(f"Програма тренувань: {training_program.name}, Тривалість: {training_program.duration}")

    # Виводимо список всіх членів команди
    print("\nЧлени команди:")
    for member in team.get_members():
        print(f"{member.get_role()}: {member.name} - Досвід: {member.experience}")

    # Видаляємо гравця з команди
    team.remove_member(player2)
    print(f"\n{player2.name} був видалений з команди.")

    # Оновлений список членів команди
    print("\nОновлений список членів команди:")
    for member in team.get_members():
        print(f"{member.get_role()}: {member.name} - Досвід: {member.experience}")

if __name__ == "__main__":
    main()
