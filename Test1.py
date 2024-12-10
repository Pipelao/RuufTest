import math

def panelsFit(a: int, b: int, x: int, y: int) -> int:
    """
    Args:
        a (int): Panel's Height
        b (int): Panel's Width
        x (int): Roof's Height
        y (int): Roof's Width

    Returns:
        int: How many panels fit the roof
    """

    if a > x or a > y or b > x or b > y: return 0

    panelsArea = a * b

    roofsArea = x * y

    panelsFitTime = math.floor(roofsArea/panelsArea)

    return panelsFitTime


if __name__ == "__main__":

    a = int(input("Insert the panel's height: "))
    b = int(input("Insert the panel's width: "))
    x = int(input("Insert the roof's height: "))
    y = int(input("Insert the roof's width: "))

    print(f"The roof can have a total of {panelsFit(a,b,x,y)} panels")

