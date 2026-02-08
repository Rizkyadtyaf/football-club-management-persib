from user import User
from salary_service import RealSalaryService
from proxy import SalaryServiceProxy

if __name__ == "__main__":
    real = RealSalaryService()

    coach = User("eva", "coach")
    finance = User("eva", "finance")

    proxy1 = SalaryServiceProxy(real, coach)
    proxy2 = SalaryServiceProxy(real, finance)

    print("=== Coach tries ===")
    print("Salary:", proxy1.get_salary("Player A"))

    print("\n=== Finance tries ===")
    print("Salary:", proxy2.get_salary("Player A"))
