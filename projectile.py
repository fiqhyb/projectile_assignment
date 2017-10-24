import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    graphs = int(input("Amount of projectile >>"))#number of projectile to input
    legends = []#to compile information then displayed
    for arcs in range(0, graphs):
        #Variables for equation
        gravity  = 9.807
        init_vel = int(input("Enter the initial velocity (m/s) >>"))#initial velocity
        angle    = int(input("Enter the angle of projectile (degrees) >>"))#angle
        time     = (((2*init_vel)*(math.sin(math.radians(angle))))/gravity)*1000#determines the amount of flight time

        #velocity alongs x and y axis
        x_vel = (math.cos(math.radians(angle)))*init_vel
        y_vel = (math.sin(math.radians(angle)))*init_vel

        #Calculator
        x = [x_vel*(x/1000) for x in range(0, int(time))]#calculates distance
        y = [(y_vel*(x/1000))-((gravity*((x/1000)**2))/2) for x in range(0, int(time))]#calculates height

        #draw arcs
        plt.plot(x,y)
        legends.append("Velocity :"+ str(init_vel)+" m/s")

    # draws and displays graph
    plt.legend(legends)
    plt.title("Projectile Motion")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    plt.show()