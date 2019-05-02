 1/1: add 3,2
 1/2: 3+2
 1/3: 3||2
 1/4: 3|2
 1/5: print("Sumanth")
 1/6: input()
 1/7: input()
 3/1:
# global binding
a = 10
b = 20
c = 30
def plus(c, d): #binding happens during a call to a function see link provided above
    a = 0 # creates a new local variable a visible only within plus
    # the local variables c and a shadows the global variables c and a
    # so, c is whatever passed to function and a is 0 (NOT c = 30 and NOT a = 10)
    # But b is a resolved from parent scope, so b = 20
    print("a inside plus: ",a)
    print("b inside plus: ",b)
    print("c inside plus: ",c)
    e = a + b + c + d
    #loop
    for d in range(0,7): # reassignment of d happens here
        print("d inside loop: ",d)
    # d will have the last value from the loop which is 6
    print("d inside plus: ",d)
    return e
print(plus(3,5))
print("global a: ",a)
print("global b: ",b)
print("global c: ",c)
# the below two should throw an error because they are out of scope
#print(d)
#print(e)
 6/1:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes law gives the force applied on a spherical body in a viscous liquid")
η = float(input("Enter the value of coefficient of viscosity (η): ")
r = float(input("Enter the value of radius of sphere: "))
v = float(input("Enter the value of velocity of the sphere: "))
print("The value of force applied on sphere by the liquid is "+stokes_law(η, r, v)+ " N")
 6/2:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes law gives the force applied on a spherical body in a viscous liquid")
η = float(input("Enter the value of coefficient of viscosity (η): "))
r = float(input("Enter the value of radius of sphere: "))
v = float(input("Enter the value of velocity of the sphere: "))
print("The value of force applied on sphere by the liquid is "+stokes_law(η, r, v)+ " N")
 8/1:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes law gives the force applied on a spherical body in a viscous liquid")
η = float(input("Enter the value of coefficient of viscosity (η): "))
r = float(input("Enter the value of radius of sphere: "))
v = float(input("Enter the value of velocity of the sphere: "))
print("The value of force applied on sphere by the liquid is "+stokes_law(η, r, v)+ " N")
 9/1:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes' law gives the force applied on a spherical body in a viscous liquid:")
η = float(input("Enter the value of coefficient of viscosity (η): "))
r = float(input("Enter the value of radius of sphere: "))
v = float(input("Enter the value of velocity of the sphere: "))
print("The value of force applied on sphere by the liquid is "+stokes_law(η, r, v)+ " N")
10/1:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes' law gives the force applied on a spherical body in a viscous liquid:")
η = float(input("Enter the value of coefficient of viscosity (η): "))
r = float(input("Enter the value of radius of sphere: "))
v = float(input("Enter the value of velocity of the sphere: "))
print("The value of force applied on sphere by the liquid is "+stokes_law(η, r, v)+ " N")
10/2:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes' law gives the force applied on a spherical body in a viscous liquid:")
η = float(input("Enter the value of coefficient of viscosity (η): "))
r = float(input("Enter the value of radius of sphere: "))
v = float(input("Enter the value of velocity of the sphere: "))
print("The value of force applied on sphere by the liquid is "+str(stokes_law(η, r, v))+ " N")
10/3:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes' law gives the force applied on a spherical body in a viscous liquid:")
η = float(input("Enter the value of coefficient of viscosity (η): "))
r = float(input("Enter the value of radius of sphere (in m): "))
v = float(input("Enter the value of velocity of the sphere(in m/s): "))
print("The value of force applied on sphere by the liquid is "+str(stokes_law(η, r, v))+ " N")
10/4:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes' law gives the force applied on a spherical body in a viscous liquid:\n")
η = float(input("Enter the value of coefficient of viscosity (η): "))
r = float(input("Enter the value of radius of sphere (in m): "))
v = float(input("Enter the value of velocity of the sphere(in m/s): "))
print("The value of force applied on sphere by the liquid is "+str(stokes_law(η, r, v))+ " N")
10/5:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes' law gives the force applied on a spherical body in a viscous liquid:\n")
η = float(input("Enter the value of coefficient of viscosity (η): "))
r = float(input("Enter the value of radius of sphere (in m): "))
v = float(input("Enter the value of velocity of the sphere(in m/s): \n"))
print("The value of force applied on sphere by the liquid is "+str(stokes_law(η, r, v))+ " N")
10/6:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes' law gives the force applied on a spherical body in a viscous liquid:\n")
η = float(input("Enter the value of coefficient of viscosity (η): "))
r = float(input("Enter the value of radius of sphere (in m): "))
v = float(input("Enter the value of velocity of the sphere(in m/s): "))
print("\nThe value of force applied on sphere by the liquid is "+str(stokes_law(η, r, v))+ " N")
10/7:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes' law gives the force applied on a spherical body in a viscous liquid:\n")
η = float(input("\tEnter the value of coefficient of viscosity (η): "))
r = float(input("\tEnter the value of radius of sphere (in m): "))
v = float(input("\tEnter the value of velocity of the sphere(in m/s): "))
print("\n\tThe value of force applied on sphere by the liquid is "+str(stokes_law(η, r, v))+ " N")
10/8:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
print("Stokes' law gives the force applied on a spherical body in a viscous liquid.\n")
η = float(input("\tEnter the value of coefficient of viscosity (η): "))
r = float(input("\tEnter the value of radius of sphere (in m): "))
v = float(input("\tEnter the value of velocity of the sphere(in m/s): "))
print("\n\tThe value of force applied on sphere by the liquid is "+str(stokes_law(η, r, v))+ " N")
10/9:
def stefan_boltzmann_law(σ, e, A, T):
    P = σ*e*A*(T**4)
    return P
print("Stefan-Boltzmann law gives the power of heat generated by a material at a given temperature.\n")
σ = 5.67E-8
e = float(input("Enter the value of emissivity(e):"))
A = float(input("Enter the surface area (in m-squared): "))
T = float(input("Enter the temperature (in K): "))

print("\nThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(σ, e, A, T) + "W")
10/10:
def stefan_boltzmann_law(σ, e, A, T):
    P = σ*e*A*(T**4)
    return P
print("Stefan-Boltzmann law gives the power of heat generated by a material at a given temperature.\n")
σ = 5.67E-8
e = float(input("Enter the value of emissivity(e):"))
A = float(input("Enter the surface area (in m-squared): "))
T = float(input("Enter the temperature (in K): "))

print("\nThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(σ, e, A, T)) + " W")
10/11:
def stefan_boltzmann_law(σ, e, A, T):
    P = σ*e*A*(T**4)
    return P
print("Stefan-Boltzmann law gives the power of heat generated by a material at a given temperature.\n")
σ = 5.67E-8
e = float(input("\tEnter the value of emissivity(e):"))
A = float(input("\tEnter the surface area (in m-squared): "))
T = float(input("\tEnter the temperature (in K): "))

print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(σ, e, A, T)) + " W")
10/12:
def drift_velocity(i, n, e, A):
    v= i/(n*A*e)
    return v
print("Velocity of the electron can be calculated for a given current , cross sectional area, number density.\n")
i = float(input("\tEnter the value of current (in A)"))
n = int(input("\tEnter the value of electron density(n)"))
A = float(input("\tEnter the value of cross-sectional area of the conductor(in m-squared): "))
e = 1.6E-19

print("\n\tThe value of mean drift velocity of electron flowing in the current is "+ str(drift_velocity) + " m/s")
10/13:
def drift_velocity(i, n, e, A):
    v= i/(n*A*e)
    return v
print("Velocity of the electron can be calculated for a given current , cross sectional area, number density.\n")
i = float(input("\tEnter the value of current (in A)"))
n = int(input("\tEnter the value of electron density(n)"))
A = float(input("\tEnter the value of cross-sectional area of the conductor(in m-squared): "))
e = 1.6E-19

print("\n\tThe value of mean drift velocity of electron flowing in the current is "+ str(drift_velocity(i, n, e, A)) + " m/s")
11/1:
def drift_velocity(i, n, e, A):
    v= i/(n*A*e)
    return v
print("Velocity of the electron can be calculated for a given current , cross sectional area, number density.\n")
i = float(input("\tEnter the value of current (in A): "))
n = int(input("\tEnter the value of electron density(n): "))
A = float(input("\tEnter the value of cross-sectional area of the conductor(in m-squared): "))
e = 1.6E-19

print("\n\tThe value of mean drift velocity of electron flowing in the current is "+ str(drift_velocity(i, n, e, A)) + " m/s")
12/1:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F
η = float(input("\tEnter the value of coefficient of viscosity (η): "))
r = float(input("\tEnter the value of radius of sphere (in m): "))
v = float(input("\tEnter the value of velocity of the sphere(in m/s): "))
print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
12/2:
def stefan_boltzmann_law(σ, e, A, T):
    P = σ*e*A*(T**4)
    return P
σ = 5.67E-8
e = float(input("\tEnter the value of emissivity(e): "))
A = float(input("\tEnter the surface area (in m-squared): "))
T = float(input("\tEnter the temperature (in K): "))

print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(σ, e, A, T)) + " W")
12/3:
def drift_velocity(i, n, e, A):
    v= i/(n*A*e)
    return v
i = float(input("\tEnter the value of current (in A): "))
n = int(input("\tEnter the value of electron density(n): "))
A = float(input("\tEnter the value of cross-sectional area of the conductor(in m-squared): "))
e = 1.6E-19

print("\n\tThe value of mean drift velocity of electron flowing in the current is "+ str(drift_velocity(i, n, e, A)) + " m/s")
13/1:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F

η = float(input("\tEnter the value of coefficient of viscosity (η): "))
r = float(input("\tEnter the value of radius of sphere (in m): "))
v = float(input("\tEnter the value of velocity of the sphere(in m/s): "))

print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
13/2:
def stefan_boltzmann_law(σ, e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

e = float(input("\tEnter the value of emissivity(e): "))
A = float(input("\tEnter the surface area (in m-squared): "))
T = float(input("\tEnter the temperature (in K): "))

print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(σ, e, A, T)) + " W")
13/3:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F

η = float(input("\tEnter the value of coefficient of viscosity (η): "))
r = float(input("\tEnter the value of radius of sphere (in m): "))
v = float(input("\tEnter the value of velocity of the sphere(in m/s): "))

print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
14/1:
def stokes_law(η, r, v):
    F= 6*3.14*η*r*v
    return F

η = float(input("\tEnter the value of coefficient of viscosity (η): "))
r = float(input("\tEnter the value of radius of sphere (in m): "))
v = float(input("\tEnter the value of velocity of the sphere(in m/s): "))

print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
14/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

e = float(input("\tEnter the value of emissivity(e): "))
A = float(input("\tEnter the surface area (in m-squared): "))
T = float(input("\tEnter the temperature (in K): "))

print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
14/3:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v
i = float(input("\tEnter the value of current (in A): "))
n = int(input("\tEnter the value of electron density(n): "))
A = float(input("\tEnter the value of cross-sectional area of the conductor(in m-squared): "))


print("\n\tThe value of mean drift velocity of electron flowing in the current is "+ str(drift_velocity(i, n, A)) + " m/s")
15/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

η = float(input("\tEnter the value of coefficient of viscosity (η): "))
r = float(input("\tEnter the value of radius of sphere (in m): "))
v = float(input("\tEnter the value of velocity of the sphere(in m/s): "))

print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
15/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

e = float(input("\tEnter the value of emissivity(e): "))
A = float(input("\tEnter the surface area (in m-squared): "))
T = float(input("\tEnter the temperature (in K): "))

print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
15/3:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v
i = float(input("\tEnter the value of current (in A): "))
n = int(input("\tEnter the value of electron density(n): "))
A = float(input("\tEnter the value of cross-sectional area of the conductor(in m-squared): "))


print("\n\tThe value of mean drift velocity of electron flowing in the current is "+ str(drift_velocity(i, n, A)) + " m/s")
18/1:
import math
def sa_cone(r, h):
    sa = math.pi*r*h + math.pi*r*r
    return sa
def vol_cone(r, h):
    vol = math.pi*r*math.sqrt(r**2+ h**2) + math.pi*r*r
    return vol
def sa_cuboid(l, b, h):
    sa = 2*(l*b+ b*h + h*l)
    return sa
def vol_cuboid(l,b, h):
    vol = l*b*h
    return vol
r_cone = input("Enter the value of radius of cone:")
h_cone = input("Enter the value of height of cone:")

l_cuboid = input("Enter the value of length of cuboid:")
b_cuboid = input("Enter the value of breadth of cuboid:")
h_cuboid = input("Enter the value of height of cuboid:")

sa_cone = sa_cone(r_cone, h_cone)
sa_cuboid = sa_cuboid(r_cone, h_cone)
vol_cone = vol_cone(l_cuboid, b_cuboid, h_cuboid)
vol_cuboid = vol_cuboid(l_cuboid, b_cuboid, h_cuboid)

solid_objects_sa = {cone:sa_cone, cuboid:sa_cuboid}
solid_objects_vol = {cone:vol_cone, cuboid:vol_cuboid}

print(solid_objects_sa)
print(solid_objects_vol)
18/2:
import math
def sa_cone(r, h):
    sa = math.pi*r*h + math.pi*r*r
    return sa
def vol_cone(r, h):
    vol = math.pi*r*math.sqrt(r**2+ h**2) + math.pi*r*r
    return vol
def sa_cuboid(l, b, h):
    sa = 2*(l*b+ b*h + h*l)
    return sa
def vol_cuboid(l,b, h):
    vol = l*b*h
    return vol
r_cone = float(input("Enter the value of radius of cone:"))
h_cone = float(input("Enter the value of height of cone:"))

l_cuboid = float(input("Enter the value of length of cuboid:"))
b_cuboid = float(input("Enter the value of breadth of cuboid:"))
h_cuboid = float(input("Enter the value of height of cuboid:"))

sa_cone = sa_cone(r_cone, h_cone)
sa_cuboid = sa_cuboid(r_cone, h_cone)
vol_cone = vol_cone(l_cuboid, b_cuboid, h_cuboid)
vol_cuboid = vol_cuboid(l_cuboid, b_cuboid, h_cuboid)

solid_objects_sa = {cone:sa_cone, cuboid:sa_cuboid}
solid_objects_vol = {cone:vol_cone, cuboid:vol_cuboid}

print(solid_objects_sa)
print(solid_objects_vol)
18/3:
import math
def sa_cone(r, h):
    sa = math.pi*r*h + math.pi*r*r
    return sa
def vol_cone(r, h):
    vol = math.pi*r*math.sqrt(r**2+ h**2) + math.pi*r*r
    return vol
def sa_cuboid(l, b, h):
    sa = 2*(l*b+ b*h + h*l)
    return sa
def vol_cuboid(l,b, h):
    vol = l*b*h
    return vol
r_cone = float(input("Enter the value of radius of cone:"))
h_cone = float(input("Enter the value of height of cone:"))

l_cuboid = float(input("Enter the value of length of cuboid:"))
b_cuboid = float(input("Enter the value of breadth of cuboid:"))
h_cuboid = float(input("Enter the value of height of cuboid:"))

sa_cone = sa_cone(r_cone, h_cone)
sa_cuboid = sa_cuboid(l_cuboid, b_cuboid, h_cuboid)
vol_cone = vol_cone(r_cone, h_cone)
vol_cuboid = vol_cuboid(l_cuboid, b_cuboid, h_cuboid)

solid_objects_sa = {cone:sa_cone, cuboid:sa_cuboid}
solid_objects_vol = {cone:vol_cone, cuboid:vol_cuboid}

print(solid_objects_sa)
print(solid_objects_vol)
18/4:
import math
def sa_cone(r, h):
    sa = math.pi*r*h + math.pi*r*r
    return sa
def vol_cone(r, h):
    vol = math.pi*r*math.sqrt(r**2+ h**2) + math.pi*r*r
    return vol
def sa_cuboid(l, b, h):
    sa = 2*(l*b+ b*h + h*l)
    return sa
def vol_cuboid(l,b, h):
    vol = l*b*h
    return vol
r_cone = float(input("Enter the value of radius of cone:"))
h_cone = float(input("Enter the value of height of cone:"))

l_cuboid = float(input("Enter the value of length of cuboid:"))
b_cuboid = float(input("Enter the value of breadth of cuboid:"))
h_cuboid = float(input("Enter the value of height of cuboid:"))

sa_cone = sa_cone(r_cone, h_cone)
sa_cuboid = sa_cuboid(l_cuboid, b_cuboid, h_cuboid)
vol_cone = vol_cone(r_cone, h_cone)
vol_cuboid = vol_cuboid(l_cuboid, b_cuboid, h_cuboid)

solid_objects_sa = {"cone":sa_cone, "cuboid":sa_cuboid}
solid_objects_vol = {"cone":vol_cone, "cuboid":vol_cuboid}

print(solid_objects_sa)
print(solid_objects_vol)
18/5:
import math
def sa_cone(r, h):
    sa = math.pi*r*h + math.pi*r*r
    return sa
def vol_cone(r, h):
    vol = math.pi*r*math.sqrt(r**2+ h**2) + math.pi*r*r
    return vol
def sa_cuboid(l, b, h):
    sa = 2*(l*b+ b*h + h*l)
    return sa
def vol_cuboid(l,b, h):
    vol = l*b*h
    return vol
r_cone = float(input("Enter the value of radius of cone:"))
h_cone = float(input("Enter the value of height of cone:"))

l_cuboid = float(input("Enter the value of length of cuboid:"))
b_cuboid = float(input("Enter the value of breadth of cuboid:"))
h_cuboid = float(input("Enter the value of height of cuboid:"))

sa_cone = sa_cone(r_cone, h_cone)
sa_cuboid = sa_cuboid(l_cuboid, b_cuboid, h_cuboid)
vol_cone = vol_cone(r_cone, h_cone)
vol_cuboid = vol_cuboid(l_cuboid, b_cuboid, h_cuboid)

solid_objects_sa = {"cone":sa_cone, "cuboid":sa_cuboid}
solid_objects_vol = {"cone":vol_cone, "cuboid":vol_cuboid}

print("Surface area in dictionary: " + solid_objects_sa)
print("Volume in dictionary: " + solid_objects_vol)
18/6:
import math
def sa_cone(r, h):
    sa = math.pi*r*h + math.pi*r*r
    return sa
def vol_cone(r, h):
    vol = math.pi*r*math.sqrt(r**2+ h**2) + math.pi*r*r
    return vol
def sa_cuboid(l, b, h):
    sa = 2*(l*b+ b*h + h*l)
    return sa
def vol_cuboid(l,b, h):
    vol = l*b*h
    return vol
r_cone = float(input("Enter the value of radius of cone:"))
h_cone = float(input("Enter the value of height of cone:"))

l_cuboid = float(input("Enter the value of length of cuboid:"))
b_cuboid = float(input("Enter the value of breadth of cuboid:"))
h_cuboid = float(input("Enter the value of height of cuboid:"))

sa_cone = sa_cone(r_cone, h_cone)
sa_cuboid = sa_cuboid(l_cuboid, b_cuboid, h_cuboid)
vol_cone = vol_cone(r_cone, h_cone)
vol_cuboid = vol_cuboid(l_cuboid, b_cuboid, h_cuboid)

solid_objects_sa = {"cone":sa_cone, "cuboid":sa_cuboid}
solid_objects_vol = {"cone":vol_cone, "cuboid":vol_cuboid}

print("Surface area in dictionary: ")
print(solid_objects_sa)
print("Volume in dictionary: ")  
print(solid_objects_vol)
18/7:
import math
def sa_cone(r, h):
    sa = math.pi*r*h + math.pi*r*r
    return sa
def vol_cone(r, h):
    vol = math.pi*r*math.sqrt(r**2+ h**2) + math.pi*r*r
    return vol
def sa_cuboid(l, b, h):
    sa = 2*(l*b+ b*h + h*l)
    return sa
def vol_cuboid(l,b, h):
    vol = l*b*h
    return vol
r_cone = float(input("Enter the value of radius of cone:"))
h_cone = float(input("Enter the value of height of cone:"))

l_cuboid = float(input("Enter the value of length of cuboid:"))
b_cuboid = float(input("Enter the value of breadth of cuboid:"))
h_cuboid = float(input("Enter the value of height of cuboid:"))

sa_cone = sa_cone(r_cone, h_cone)
sa_cuboid = sa_cuboid(l_cuboid, b_cuboid, h_cuboid)
vol_cone = vol_cone(r_cone, h_cone)
vol_cuboid = vol_cuboid(l_cuboid, b_cuboid, h_cuboid)

solid_objects_sa = {"cone":sa_cone, "cuboid":sa_cuboid}
solid_objects_vol = {"cone":vol_cone, "cuboid":vol_cuboid}

print("\nSurface area in dictionary: ")
print(solid_objects_sa)
print("Volume in dictionary: ")  
print(solid_objects_vol)
19/1:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f=f.readline()
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/3:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/4:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.read()
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/5:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.read()
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/6:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.read()
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/7:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.read()
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/8:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.read()
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/9:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")

for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/10:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.read()
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/11:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,1)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/12:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(1,0)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/13:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,2)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/14:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,2)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/15:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,1)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/16:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,2)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/17:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,2)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/18:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,2)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/19:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,3)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/20:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(1,1)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/21:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,1)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/22:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,1)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/23:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,1)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/24:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,1)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/25:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stokes.txt", "r")
f.seek(0,1)
for line in f:
    print(line)

#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
19/26:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.seek(0,1)
for line in f:
    print(line)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/27:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
x= f.readline()
for line in f:
    print(line)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/28:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
x= f.readline()
for line in x:
    print(line)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/29:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
x= f.readline()
for line in f:
    print(line)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/30:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
for line in f:
    print(line)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/31:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    print(line)
    c+=1
print(c)  

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/32:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    print(line)
    c+=1
print(c)  

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/33:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    print(line)
    c+=1
print(c)  

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/34:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/35:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/36:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    l= line.split("=")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/37:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    l= line.split("=")
    if l[0]="η":
        print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/38:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    l= line.split("=")
    #if l[0]="η":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/39:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    l= line.split("=")
    if l[0]="Î·":
        print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/40:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    l= line.split("=")
    if l[0]=="η":
        print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/41:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
for line in f:
    l= line.split("=")
    if l[0]=="Î·":
        print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/42:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
print(values)
for line in f:
    l= line.split("=")
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/43:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
print(values.keys())
for line in f:
    l= line.split("=")
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/44:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
print(values.values())
for line in f:
    l= line.split("=")
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/45:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
print(values.value())
for line in f:
    l= line.split("=")
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/46:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
print(values.values())
for line in f:
    l= line.split("=")
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/47:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values.values())
for line in f:
    l= line.split("=")
    for f in values:
        print(f)
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/48:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values.values())
for line in f:
    l= line.split("=")
    for i in values:
        print(i)
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/49:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values.values())
for line in f:
    l= line.split("=")
    for i in values:
        print(values[i])
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/50:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values.values())
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[1]
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)
print(values)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/51:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values.values())
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)
print(values)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/52:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values.values())
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #if l[0]=="Î·":
    #    print("Yeah! It is η.")
    print(l)
    print(line)
    c+=1
print(c)
print(values)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/53:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    print(l)
    print(line)
    c+=1
print(c)
print(values)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/54:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
c=0
f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
    c+=1
print(c)
print(values)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/55:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
    c+=1
print(values)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/56:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
    c+=1
#print(values)

#print("\n\tThe value of force applied on sphere by the liquid is "+ str(stokes_law(η, r, v))+ " N")
19/57:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
    c+=1
#print(values)

F= stokes_law(float(values[η]), float(values[r]), float(values[v])

print("\n\tThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
19/58:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
    c+=1
#print(values)

F= stokes_law(float(values[η]), float(values[r]), float(values[v])
print("\n\tThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
19/59:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
    c+=1
#print(values)

F= stokes_law(float(values[η]), float(values[r]), float(values[v])
print("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
    c+=1
#print(values)

F= stokes_law(float(values[η]), float(values[r]), float(values[v])
print("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/2:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
    c+=1
#print(values)
f.close()

F= stokes_law(float(values[η]), float(values[r]), float(values[v])
print("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/3:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
    c+=1
#print(values)
f.close()

F= stokes_law(float(values[η]), float(values[r]), float(values[v]))
print("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/4:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
#print(values)
f.close()

F= stokes_law(float(values[η]), float(values[r]), float(values[v]))
print("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/5:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
#print(values)
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
    #print(l)
    #print(line)
#print(values)
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
print("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/6:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
f=open("stokes.txt", "a")
f.print("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/7:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
f=open("stokes.txt", "a")
f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/8:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/9:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
22/10:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan-boltzmann.txt", "a") as f:


#print("\n\tThe value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
22/11:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan-boltzmann.txt", "a") as f:
    f.write("The value of power released by the material (ΔQ/Δt): "+ str(stefan_boltzmann_law(e, A, T)) + " W")
22/12:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

P= stokes_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan-boltzmann.txt", "a") as f:
    f.write("The value of power released by the material (ΔQ/Δt): "+ str(P) + " W")
23/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("The value of force applied on sphere by the liquid is "+ str(F)+ " N")
23/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

P= stokes_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan-boltzmann.txt", "a") as f:
    f.write("The value of power released by the material (ΔQ/Δt): "+ str(P) + " W")
23/3:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan-boltzmann.txt", "a") as f:
    f.write("The value of power released by the material (ΔQ/Δt): "+ str(P) + " W")
23/4:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
print(values)
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
#with open("stefan-boltzmann.txt", "a") as f:
#    f.write("The value of power released by the material (ΔQ/Δt): "+ str(P) + " W")
23/5:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
print(values)
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan-boltzmann.txt", "a") as fle:
    fle.write("The value of power released by the material (ΔQ/Δt): "+ str(P) + " W")
23/6:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
print(values)
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
print(P)
#with open("stefan-boltzmann.txt", "a") as fle:
#    fle.write("The value of power released by the material (ΔQ/Δt): "+ str(P) + " W")
23/7:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
print(values)
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
print(P)
with open("stefan-boltzmann.txt", "a") as fle:
    fle.write("The value of power released by the material (ΔQ/Δt): "+ str(P) + " W")
23/8:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
print(values)
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
print(P)
with open("stefan-boltzmann.txt", "a") as fle:
    fle.write("The value of power released by the material : "+ str(P) + " W")
23/9:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
23/10:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
print(values)
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
print(P)
with open("stefan-boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
23/11:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
print(values)
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
print(P)
with open("stefan-boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
23/12:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan-boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
23/13:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan-boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
23/14:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    print("\n\tThe value of mean drift velocity of electron flowing in the current is "+ str(drift_velocity(i, n, A)) + " m/s")
23/15:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    print("\n\tThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
23/16:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    f.write("\n\tThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
23/17:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    f.write("\nThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
25/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
25/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan-boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan-boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
25/3:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    f.write("\nThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
26/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
26/2:
import math

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan-boltzmann_values={"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v
def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan-boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": write_result_in_file  }
    result = formulae[file_name](*values[value])
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan-boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan-boltzmann.txt",stefan-boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
26/3:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan-boltzmann_values={"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan-boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": write_result_in_file  }
    result = formulae[file_name](*values[value])
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan-boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan-boltzmann.txt",stefan-boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
26/4:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan-boltzmann_value = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan-boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": write_result_in_file  }
    result = formulae[file_name](*values[value])
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan-boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan-boltzmann.txt",stefan-boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
26/5:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan-boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan-boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": write_result_in_file  }
    result = formulae[file_name](*values[value])
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan-boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan-boltzmann.txt",stefan-boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/1:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan-boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": write_result_in_file  }
    result = formulae[file_name](*values[value])
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan-boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan-boltzmann.txt",stefan-boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/2:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": write_result_in_file  }
    result = formulae[file_name](*values[value])
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan-boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/3:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": write_result_in_file  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan-boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/4:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": write_result_in_file  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/5:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": write_result_in_file  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/6:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/7:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/8:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/9:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan_boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan_boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
27/10:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        if file_name==writing:
            print(writing[value])
            fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/11:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[value])
                fle.write(writing[value])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/12:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/13:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/14:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/15:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/16:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/17:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    except:
        print("The file {} is not available.".format(file_name))
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/18:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    except:
        print("The file {} is not available.".format(file_name))
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokeas.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/19:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    except:
        print("The file {} is not available.".format(file_name))
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/20:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    except:
        print("The file {} is not available.".format(file_name))
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/21:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    except:
        print("The file {} is not available.".format(file_name))
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    for value in values:
        values[value]= float(values[value])
        
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    
    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/22:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }

        #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
    except:
        print("The file {} is not available.".format(file_name))                

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/23:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        try:
            result = formulae[file_name](*values.values())
        
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }

            #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("Sorry.. inputs must be numeric.")            
    except:
        print("The file {} is not available.".format(file_name))                

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/24:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        try:
            result = formulae[file_name](*values.values())
        
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }

            #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("Sorry.. inputs must be numeric.")            
    except:
        print("The file {} is not available.".format(file_name))                

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/25:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        try:
            result = formulae[file_name](*values.values())
        
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }

            #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("Sorry.. inputs must be numeric.")            
    except:
        print("Sorry.. The file {} is not available.".format(file_name))                

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/26:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
        
    for value in values:
        values[value]= float(values[value])

    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }

    result = formulae[file_name](*values.values())

    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/27:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
        
    for value in values:
        values[value]= float(values[value])

    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    try:
        result = formulae[file_name](*values.values())
    except:
        print("Sorry.. The input must be numeric")

    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/28:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    try:    
        for value in values:
            values[value]= float(values[value])
    except:
        print("Sorry.. The input must be numeric")    

    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    

    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/29:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    try:    
        for value in values:
            values[value]= float(values[value])
        result = formulae[file_name](*values.values())
        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
    except:
        print("Sorry.. The input must be numeric")    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/30:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    try:    
        for value in values:
            values[value]= float(values[value])
        result = formulae[file_name](*values.values())
        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
    except:
        print("Sorry.. The input must be numeric")    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/31:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    #try:
    for value in values:
        values[value]= float(values[value])
    result = formulae[file_name](*values.values())
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
    #except:
    #    print("Sorry.. The input must be numeric")  

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/32:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    #try:
    for value in values:
        values[value]= float(values[value])
    result = formulae[file_name](*values.values())
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
    #except:
    #    print("Sorry.. The input must be numeric")  

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
27/33:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    #try:
    for value in values:
        values[value]= float(values[value])
    result = formulae[file_name](*values.values())
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
    #except:
    #    print("Sorry.. The input must be numeric")  

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
28/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
28/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan_boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan_boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
28/3:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    f.write("\nThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
28/4:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    #try:
    for value in values:
        values[value]= float(values[value])
    result = formulae[file_name](*values.values())
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
    #except:
    #    print("Sorry.. The input must be numeric")  

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
29/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan_boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan_boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
29/3:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    f.write("\nThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
29/4:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    #try:
    for value in values:
        values[value]= float(values[value])
    result = formulae[file_name](*values.values())
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
    #except:
    #    print("Sorry.. The input must be numeric")  

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/5:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    try:
        for value in values:
            values[value]= float(values[value])
        result = formulae[file_name](*values.values())
        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
    except:
        print("Sorry.. The input must be numeric")     
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/6:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    try:
        for value in values:
            values[value]= float(values[value])
        result = formulae[file_name](*values.values())
        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
    except:
        print("Sorry.. The input must be numeric")     
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/7:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
    except:
        print("The file {} is not available.".format(file_name))
    #try:
    for value in values:
        values[value]= float(values[value])
    result = formulae[file_name](*values.values())
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
    #except:
    #    print("Sorry.. The input must be numeric")     
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/8:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])
        result = formulae[file_name](*values.values())
        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
    except:
        print("The file {} is not available.".format(file_name))
    
    #except:
    #    print("Sorry.. The input must be numeric")     
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/9:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])
        result = formulae[file_name](*values.values())
        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
    except:
        print("The file {} is not available.".format(file_name))
    
    #except:
    #    print("Sorry.. The input must be numeric")     
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/10:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")
    
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])
        result = formulae[file_name](*values.values())
        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
    except:
        print("The file {} is not available.".format(file_name))
    
    #except:
    #    print("Sorry.. The input must be numeric")     
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/11:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
    f=open(file_name, "r")

    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    #try:
    for value in values:
        values[value]= float(values[value])
    result = formulae[file_name](*values.values())
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
    #except:
     #   print("The file {} is not available.".format(file_name))
    
    #except:
    #    print("Sorry.. The input must be numeric")     
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/12:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
    f=open(file_name, "r")

    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    #try:
    for value in values:
        values[value]= float(values[value])
    
    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
    #except:
     #   print("The file {} is not available.".format(file_name))
    
    #except:
    #    print("Sorry.. The input must be numeric")     
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/13:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")

        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
    except:
        print("The file {} is not available.".format(file_name))
    
    #except:
    #    print("Sorry.. The input must be numeric")     
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/14:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")

        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
    except:
        print("The file {} is not available.".format(file_name))
    
    #except:
    #    print("Sorry.. The input must be numeric")     
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/15:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")

        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
             print("Sorry.. The input must be numeric")               
    except:
        print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/16:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    try:
        f=open(file_name, "r")

        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    except:
        print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/17:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open(file_name, "r")

        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/18:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open(file_name, "r")

        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/19:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open(file_name, "r")

        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/20:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open(file_name, "r")

        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    values[key]+=1
                    values[key]-=1
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/21:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open(file_name, "r")

        print(f.readline())
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    values[key]+=1
                    values[key]-=1
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
29/22:
import math
def satokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
29/23:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("satokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
29/24:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
29/25:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open(file_name, "r")

        print(f.readline())
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    values[key]+=1
                    values[key]-=1
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
30/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan_boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan_boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
30/3:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    f.write("\nThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
30/4:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open(file_name, "r")

        print(f.readline())
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/5:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open("stokes.txt", "r")

        print(f.readline())
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokaes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/6:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open(file_name, "r")

        print(f.readline())
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/7:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
        f=open(file_name, "r")

        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/8:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    #try:
    for value in values:
        values[value]= float(values[value])

    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/9:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    #try:
    f=open(file_name, "r")
    f.readline()
    for line in f:
        l= line.split("=")
        for key in values:
            if values[key]==l[0]:
                values[key]=l[1].split("\n")[0]
                break
    f.close()
    #try:
    for value in values:
        values[value]= float(values[value])

    formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
    result = formulae[file_name](*values.values())
    writing={
        "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
        "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
        "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
    }
    with open(file_name, "a") as fle:
        for key in writing:    
            if file_name==key:
                print(writing[key])
                fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/10:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values):
    
    f=open(file_name, "r")
    f.readline()
    
    try:
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    except:
        print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/11:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    except:
        print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/12:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    #try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        #try:
        for value in values:
            values[value]= float(values[value])

        formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
        result = formulae[file_name](*values.values())
        writing={
            "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
            "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
            "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
        }
        with open(file_name, "a") as fle:
            for key in writing:    
                if file_name==key:
                    print(writing[key])
                    fle.write(writing[key])
        #except:
        #    print("Sorry.. The input must be numeric")               
    #except:
    #    print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/13:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("Sorry.. The input must be numeric")               
    except:
        print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/14:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("Sorry.. The input must be numeric")               
    except:
        print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/15:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("Sorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("The file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/16:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("\nSorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("\nThe file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/17:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("\nSorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("\nThe file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/18:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("\nSorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("\nThe file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/19:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("\nSorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("\nThe file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("staokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/20:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("\nSorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("\nThe file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/21:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("\nSorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("\nThe file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
30/22: #Batch input of three files taken all at once with exceptions covered.
31/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
31/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan_boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan_boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
31/3:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    f.write("\nThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
31/4: #Batch input of three files taken all at once with exceptions covered.
31/5:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("\nSorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("\nThe file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
32/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
32/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan_boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan_boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
32/3:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    f.write("\nThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
32/4:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("\nSorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("\nThe file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
33/1:
import math
def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F

f=open("stokes.txt", "r")
f.readline()
values={"η":"Î·", "r":"r", "v":"v"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

F= stokes_law(float(values["η"]), float(values["r"]), float(values["v"]))
with open("stokes.txt", "a") as f:
    f.write("\nThe value of force applied on sphere by the liquid is "+ str(F)+ " N")
33/2:
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P

f=open("stefan_boltzmann.txt", "r")
f.readline()
values={"e":"e", "A":"A", "T":"T"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()
P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
with open("stefan_boltzmann.txt", "a") as fle:
    fle.write("\nThe value of power released by the material : "+ str(P) + " W")
33/3:
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

f=open("driftvel.txt", "r")
f.readline()
values={"i":"i", "n":"n", "A":"A"}
for line in f:
    l= line.split("=")
    for key in values:
        if values[key]==l[0]:
            values[key]=l[1].split("\n")[0]
            break
f.close()

v= drift_velocity(float(values["i"]), float(values["n"]), float(values["A"]))
with open("driftvel.txt", "a") as f:
    f.write("\nThe value of mean drift velocity of electron flowing in the current is "+ str(v) + " m/s")
33/4:
import math

def stokes_law(η, r, v):
    F= 6*math.pi*η*r*v
    return F
def stefan_boltzmann_law(e, A, T):
    σ = 5.67E-8
    P = σ*e*A*(T**4)
    return P
def drift_velocity(i, n, A):
    e = 1.6E-19
    v= i/(n*A*e)
    return v

stokes_values={"η":"Î·", "r":"r", "v":"v"}
stefan_boltzmann_values = {"e":"e", "A":"A", "T":"T"}
driftvel_values={"i":"i", "n":"n", "A":"A"}

def write_result_in_file(file_name,values): 
    try:
        f=open(file_name, "r")
        f.readline()
        for line in f:
            l= line.split("=")
            for key in values:
                if values[key]==l[0]:
                    values[key]=l[1].split("\n")[0]
                    break
        f.close()
        try:
            for value in values:
                values[value]= float(values[value])

            formulae={"stokes.txt": stokes_law, "stefan_boltzmann.txt": stefan_boltzmann_law, "driftvel.txt": drift_velocity  }
            result = formulae[file_name](*values.values())
            writing={
                "stokes.txt": ("\nThe value of force applied on sphere by the liquid is "+ str(result)+ " N"), 
                "stefan_boltzmann.txt" : ("\nThe value of power released by the material : "+ str(result) + " W") , 
                "driftvel.txt" : ("\nThe value of mean drift velocity of electron flowing in the current is "+ str(result) + " m/s")
            }
            with open(file_name, "a") as fle:
                for key in writing:    
                    if file_name==key:
                        print(writing[key])
                        fle.write(writing[key])
        except:
            print("\nSorry.. the input given in the file must be numeric. Check the file inputs again.")               
    except:
        print("\nThe file {} is not available.".format(file_name))
    
         
    
    

    

    #P= stefan_boltzmann_law(float(values["e"]), float(values["A"]), float(values["T"]))
    
                    

        
write_result_in_file("stokes.txt",stokes_values)
write_result_in_file("stefan_boltzmann.txt",stefan_boltzmann_values)
write_result_in_file("driftvel.txt",driftvel_values)
37/1:
import mysql.connector as sql
import pandas as pd
37/2:
import mysql.connector as sql
import pandas as pd
37/3:
#What if it already exist?
mycursor.execute("CREATE DATABASE IF NOT EXISTS ase1")
37/4:
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
37/5:
mydb = sql.connect(
  host="localhost",
  user="root",
  passwd="mysql"
)
37/6:
import mysql.connector as sql
import pandas as pd
37/7: db_connection = sql.connect(host='localhost', database='world', user='root', password='mysql')
38/1:
import mysql.connector as sql
import pandas as pd
38/2: db_connection = sql.connect(host='localhost', database='world', user='root', password='mysql')
38/3:
import mysql.connector as sql
import pandas as pd
38/4: db_connection = sql.connect(host='localhost', database='world', user='root', password='mysql')
38/5: df = pd.read_sql('SELECT * FROM country', con=db_connection)
38/6: db_connection = sql.connect(host='localhost', database='world', user='root', password='mysql')
39/1:
import mysql.connector as sql
import pandas as pd
39/2: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/3: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/4: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/5: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/6: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/7: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/8: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/9: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/10: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/11: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/12: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/13: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
39/14: db_connection = sql.connect(host='localhost', database='world', user='root', password='mysql')
40/1:
# Double quotes
"Hello guys"
40/2:
# Single quotes
'Tired already?'
40/3:
# type the built-in function
type("Hello guys")
40/4:
#testing autocomplete and help
str.find
40/5: "hello".upper()
40/6:
sri = '{} is hot and humid'.format('Sri City')
print(sri)
40/7:
sri = 'is it {} or {}?'.format('Sri City', 'Sricity')
print(sri)
40/8: print('My name is {} {}, I go by {}.'.format('Balasubramanian', 'Kandaswamy', 'Subu'))
40/9: print('There are {first} you can do with {second}, you can learn them {third}.'.format(first='much more', second='format', third='online'))
40/10:
my_int = 6
print('value: {}, type: {}'.format(my_int, type(my_int)))
40/11:
# Remember that you should never do this This is only for demonstration
my_bool = True
print(my_bool + my_int)
40/12:
test = []
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = 0.0
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = my_bool
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))
40/13:
# example
t_list = []
if t_list:
    print("I Exist!")
else:
    print("I Dont Exist!")
40/14:
my_float = float(my_int)
print('value: {}, type: {}'.format(my_float, type(my_float)))
40/15:
# Divide operation converts to float
print(1 / 1)
print(6 / 5)
40/16:
my_string = "Please do your assignments. Please! "
len(my_string)
40/17: my_string.strip()[-1]
40/18:
# Remember its immutable
my_string.replace('a', 'A')
40/19: print(my_string)
40/20:
#method chaining example
print(my_string.strip().lower().replace('assignments', 'homeworks'))
40/21: k = (1,'two',3.0)
40/22:
print(len(k))
print(k[1])
print(k[1:3])
40/23:
# very useful when returning multiple values from a function
(a,b,c,d) = k
40/24: k = (1,'two',3.0)
40/25:
# very useful when returning multiple values from a function
(a,b,c,d) = k
40/26: b
40/27:
#Empty List
my_empty_list = []
print('empty list: {}, type: {}'.format(my_empty_list, type(my_empty_list)))
print(' am I True?:{}'.format(bool(my_empty_list)))
40/28:
#Accessing by index
my_list = ['Python', 'is', 'still', 'cool']
print(my_list[0])
print(my_list[-1])
40/29:
#Multi dimensional
coordinates = [[12.0, 13.3], [0.6, 18.0], [88.0, 1.1]]  # two dimensional
print('first coordinate: {}'.format(coordinates[0]))
print('second element of first coordinate: {}'.format(coordinates[0][1]))
40/30:
#Mutability
my_list = [0, 1, 2, 3, 4, 5]
my_list[0] = 99
print(my_list)

# remove first value
del my_list[0]
print(my_list)
40/31:
numbers = [8, 1, 6, 5, 10]
sorted_numbers = sorted(numbers)
print('numbers: {}, sorted: {}'.format(numbers, sorted_numbers))
40/32:
first_list = ['beef', 'ham']
second_list = ['potatoes',1 ,3]
first_list.extend(second_list)
print('first: {}, second: {}'.format(first_list, second_list))
40/33:
first = [1, 2, 3]
second = [4, 5]
first += second  # same as: first = first + second
print('first: {}'.format(first))

# If you need a new list
summed = first + second
print('summed: {}'.format(summed))
40/34:
my_list = ['a', 'b', 'ham']
my_list.reverse()
print(my_list)
40/35: stack = [3, 4, 5]
40/36: stack = [3, 4, 5]
40/37:
stack.append(6)
print(stack)
40/38: stack.pop()
40/39: stack.pop()
40/40: stack.pop()
40/41: stack.pop()
40/42: stack.pop()
40/43: stack.pop()
40/44:
stack.append(6)
print(stack)
40/45: stack.pop()
40/46: stack.pop()
40/47:
#Initialization
dict1 = {'value1': 1.6, 'value2': 10, 'name': 'John Doe'}
dict2 = dict(value1=1.6, value2=10, name='John Doe')

print(dict1)
print(dict2)

print('equal: {}'.format(dict1 == dict2))
print('length: {}'.format(len(dict1)))
40/48:
#Listing all keys, values and items
print('keys: {}'.format(dict1.keys()))
print('values: {}'.format(dict1.values()))
print('items: {}'.format(dict1.items()))
40/49:
#Deleting a Value
my_dict = {'key1': 'value1', 'key2': 99, 'keyX': 'valueX'}
del my_dict['keyXS']
print(my_dict)
# what happens when the key doesn't exist
40/50:
#Deleting a Value
my_dict = {'key1': 'value1', 'key2': 99, 'keyX': 'valueX'}
del my_dict['keyX']
print(my_dict)
# what happens when the key doesn't exist
40/51:
# Usually better to make sure that the key exists (see also pop() and popitem())
key_to_delete = 'my_key'
if key_to_delete in my_dict:
    del my_dict[key_to_delete]
print(my_dict)
# We'll look into the 'in' operator next class
40/52:
x = set("A Python Tutorial")
print (x)
41/1:
import mysql.connector as sql
import pandas as pd
41/2: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
41/3: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
41/4:
import mysql.connector as sql
import pandas as pd
41/5: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
41/6:
import mysql.connector as sql
import pandas as pd
41/7: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
41/8: df = pd.read_sql('SELECT * FROM country', con=db_connection)
41/9: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
41/10:
import mysql.connector as sql
import pandas as pd
41/11: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
41/12: df = pd.read_sql('SELECT * FROM country', con=db_connection)
41/13: df.head()
41/14: db_connection.close()
42/1:
import mysql.connector as sql
import pandas as pd
42/2: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
43/1:
import mysql.connector as sql
import pandas as pd
43/2: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
43/3:
import mysql.connector as sql
import pandas as pd
43/4: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
43/5: df = pd.read_sql('SELECT * FROM country', con=db_connection)
43/6:
mydb = sql.connect(
  host="localhost",
  user="root",
  passwd="Mysql@881595362672"
)
43/7:
import mysql.connector as sql
import pandas as pd
43/8: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
43/9: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
43/10:
mydb = sql.connect(
  host="localhost",
  user="root",
  passwd="Mysql@881595362672"
)
43/11: db_connection = sql.connect(host='localhost', database='world', user='root', password='mysql@881595362672')
43/12: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
43/13: db_connection = sql.connect(host='localhost', database='world', user='root', password='881595362672@Mysql')
43/14: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
43/15:
import mysql.connector as sql
import pandas as pd
43/16: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
44/1:
import mysql.connector as sql
import pandas as pd
44/2:
import mysql.connector as sql
import pandas as pd
44/3: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
45/1:
import mysql.connector as sql
import pandas as pd
45/2: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
46/1:
import mysql.connector as sql
import pandas as pd
46/2: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
46/3: df = pd.read_sql('SELECT * FROM country', con=db_connection)
46/4: df.head()
46/5: db_connection.close()
46/6:
mydb = sql.connect(
  host="localhost",
  user="root",
  passwd="Mysql@881595362672"
)
46/7:
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
46/8:
#What if it already exist?
mycursor.execute("CREATE DATABASE IF NOT EXISTS ase1")
46/9:
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
47/1: db_connection.close()
47/2:
import mysql.connector as sql
import pandas as pd
47/3: db_connection = sql.connect(host='localhost', database='world', user='root', password='Mysql@881595362672')
47/4: df = pd.read_sql('SELECT * FROM country', con=db_connection)
47/5: df.head()
47/6: db_connection.close()
47/7:
mydb = sql.connect(
  host="localhost",
  user="root",
  passwd="Mysql@881595362672"
)
47/8:
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
47/9:
#What if it already exist?
mycursor.execute("CREATE DATABASE IF NOT EXISTS ase1")
47/10:
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
51/1: print "Ipython print"
51/2: print ("Ipython print")
51/3: print
51/4: ?
51/5: q
53/1:
print('PyDev console: using IPython 6.5.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['G:\\ASE1\\ase1_prj', 'G:/ASE1/ase1_prj'])
54/1: from questions.models import QuestionView
54/2: QuestionView.objects.all().delete()
55/1: from questions.models import Submission
55/2: S = Submission.objects.all()
55/3: S
55/4: S.__dict__
55/5: S[1].delete()
56/1: from questions.models import Submission
56/2: from question.views import start_code_run_sequence()
56/3: S = SUbmission.objects.all()
56/4: S = Submission.objects.all()
56/5: start_code_run_sequence(S[0])
56/6: from question.views import start_code_run_sequence
56/7: from questions.views import start_code_run_sequence
56/8: start_code_run_sequence(S[0])
56/9: start_code_run_sequence(S[1])
56/10: 
56/11: 
56/12: 
57/1:
print('PyDev console: using IPython 6.5.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:/Users/lenovo'])
58/1:
print('PyDev console: using IPython 6.5.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['G:\\ASE1\\ase1_prj', 'G:/ASE1/ase1_prj'])
59/1: from questions.serializers import QuestionSerializer
59/2: serializer = QuestionSerializer()
59/3: print(repr(serializer))
60/1:
print('PyDev console: using IPython 6.5.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['G:\\ASE1\\ase1_prj', 'G:/ASE1/ase1_prj'])
61/1: import sys
61/2: sys.platform
61/3: import os
61/4: os.name
61/5: import platform
61/6: platform.system
61/7: platform.system
61/8: platform.system()
61/9: platform.machine()
61/10: platform.uname()
61/11: platform.macname()
61/12: platform.mac_ver()
61/13: 
61/14: 
61/15: x
62/1: from comtest.models import Contest
62/2: from contest.models import Contest
62/3: from contests.models import Contest
62/4: Contest.objects.delete()
62/5: Contest.objects.all().delete()
62/6: Contest.objects.all().delete()
63/1: from contests import models
63/2: Contest.objects.all()
63/3: models
63/4: Contest.objects.all()
63/5: Contest.objects.all().values('author')
63/6: from models import Contest
63/7: from .models import Contest
63/8: ls
63/9: from contests import models
63/10: from contests.models import Contest
63/11: Contest.objects.all()
63/12: ContestQuestion.objects.all()
63/13: from contests.models import Contest
63/14: from contests.models import ContestQuestion
63/15: ContestQuestion.objects.all()
63/16: from contests.models import Contest
63/17: ContestQuestion.objects.all().values('start_date')
63/18: Contest.objects.all().values('start_date')
63/19: Contest.objects.all()
63/20: datetime.datetime
63/21: datetime
63/22: from datetime import datetime
63/23: datetime
63/24: datetime.datetime
63/25: datetime
63/26: import datetime
63/27: datetime.datetime.time()
63/28: datetime.datetime.now()
63/29: print(datetime.datetime.now())
63/30: datetime.MINYEAR
63/31: datetime.MAXYEAR
63/32: datetime.date
63/33: datetime.time
63/34: datetime.time.now()
63/35: datetime.time.day()
63/36: datetime.day()
63/37: datetime.datetime.day()
63/38: datetime.datetime.day
63/39: datetime.datetime.day
63/40: date.today()
63/41: from datetime import date
63/42: date.today()
63/43: import time
63/44: time.now()
63/45: datetime.now()
63/46: datetime.datetime.now()
63/47: datetime.datetime.utcnow()
63/48: datetime.datetime.combine()
63/49: datetime.datetime.combine(date)
63/50: datetime.datetime.combine(datetime.date)
63/51: datetime.datetime.combine(datetime.date, datetime.time)
63/52: datetime.datetime.now().time()
63/53: datetime.now().time()
63/54: from datetime import datetime
63/55: datetime.now().time()
63/56: datetime.now("%d %B %Y %H:%M:%S")
63/57: datetime.datetime.now("%d %B %Y %H:%M:%S")
63/58: datetime.now("%d %B %Y %H:%M:%S")
63/59: dt = datetime.datetime.combine(C.start_date, C.start_time)
63/60: dt = datetime.combine(C.start_date, C.start_time)
63/61: from contests/models import Contest
63/62: from contests import Contest
63/63: from contests import models
63/64: from models import Contest
63/65: from .models import Contest
63/66: from contest.models import Contest
63/67: from . import Contest
63/68: C = Contest.objects.all().values({start_time, start_date})
63/69: C = Contest.objects.all().values(start_time)
63/70: C = Contest.objects.all().values()
63/71: C
63/72: C = Contest.objects.all().values('start_date')
63/73: C
63/74:
dt = datetime.combine(C, Contest.objects.all().values('start_time')

)
63/75: dt = datetime.combine(C, Contest.objects.all().values('start_time'))
63/76: C = Contest.objects.all().values()
63/77: dt = datetime.combine(C.start_date, C.start_time)
63/78: C
63/79: dt = datetime.combine(C.start_date, C.start_time)
63/80: C
63/81: C[start_date]
63/82: C.start_date
63/83: C.objects.values(start_date)
63/84: C.start_date
63/85: C
63/86: C.id
63/87: C('start_date')
63/88: C.start_date
63/89: datetime.now()
63/90: time.time.now()
63/91: time.now()
63/92: datetime.time.now()
63/93: datetime.all()
63/94: datetime.datetime.all()
64/1: datetime.datetime.now()
64/2: import datetime
64/3: datetime.datetime.now()
64/4: datetime.objects.all()
64/5: datetime.all()
64/6: datetime.dir()
64/7: datetime.__dir__()
64/8: django.db.__dir__()
64/9: from django import django.db
64/10: dir
64/11: ls
64/12: from contests import models
64/13: ls
64/14: from models import Contest
64/15: from contests.models import Contest
64/16: Contest.__dir__()
64/17: Contest.__dir__(all)
64/18: Contest.dir()
64/19: Contest.__dict__()
64/20: Contest.objects.all()
64/21: Contest.objects.all().values(start_time)
64/22: Contest.objects.all().values('start_time'))
64/23: Contest.objects.all().values(hellocont)
64/24: Contest.objects.all()
64/25: Contest.objects.all().values(start_date)
64/26:
Contest.objects.all().values(
)
64/27: Contest.objects.all().values('start_date')
64/28: C = Contest.objects.all()
64/29: C.values('start_date')
64/30: C.values('start_time)
64/31: C.values('start_time')
64/32: datetime.datetime.now()
64/33: datetime.datetime.now().month()
64/34: datetime.datetime.now().month
64/35: datetime.datetime.now().strftime("%d")
64/36: datetime.datetime.now().strftime("%d %B")
64/37: datetime.datetime.now().strftime("%d %A")
64/38: datetime.datetime.now().strftime("%d %C")
65/1: from contest.models import Contest
65/2: from contests.models import Contest
65/3: Contest.objects.all()
65/4: Contest.objects.all().values()
65/5: Contest.objects.all().values(start_date)
65/6: Contest.objects.all().values('start_date')
65/7: Contest.objects.all(unique_code= 'hellocont').values('start_date')
65/8: Contest.objects.filter(unique_code= 'hellocont').values('start_date')
66/1: from contests import models
66/2: from . import Contest
66/3: from .models import Contest
66/4: from contests.models import Contest
66/5: Contest.objects.all()
66/6: Contest.objects.all().start_time
66/7: Contest.objects.all().start_time()
66/8: Contest.objects.all().start_time
66/9: Contest.objects.all()
66/10: C = Contest.objects.all()
66/11: C.start_time
66/12: Contest
66/13: objects
66/14: Contest.objects.all().values('start_time')
66/15: Contest.objects.all().values('start_time').start_time
66/16: Contest.objects.all().values('start_time').values('start_time')
66/17: Contest.objects.all().
66/18: Contest.objects.all()
66/19:
for temp in Contest.objects.all():
    temp1 = temp.start_time
    print(temp1)
66/20: Contest.objects.all()
66/21: Contest.objects.all().values('start_time').start_time
66/22: Contest.objects.get('hellocont').start_time
66/23: Contest.objects.get('hellocont')
66/24: C =Contest.objects.get('hellocont')
66/25: C = Contest.objects.get(unique_id ='hellocont')
66/26: C = Contest.objects.get(unique_code ='hellocont')
66/27: C.start_date
67/1: from contests.models import Contest
67/2: c = Contest.objects.get(unique_code = 'hellocont')
67/3: c
67/4: c = Contest.objects.get(unique_code = 'hellocont')
67/5: c.start_time
67/6: import datetime
67/7: datetime.datetime.now()
67/8: datetime.datetime.now().time()
67/9: C = Contest.objects.get(unique_code ='hellocont')
67/10: C.start_date - datetime.datetime.now()
67/11: C.start_date < datetime.datetime.now()
67/12: C.start_date < datetime.now()
67/13: from datetime import datetime
67/14: C.start_date < datetime.now()
67/15: dt = datetime.now()
67/16: comb= dt.combine(dt, C.start_time)
67/17: comb
67/18: comb - datetime.now()
67/19: datetime.now() - comb
67/20: comb - datetime.now()
68/1: from contests.models import Contest
68/2: Contest.objects.all()
68/3: Contest.objects.all().values()
69/1:
print('PyDev console: using IPython 6.5.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['G:\\ASE1\\ase1_prj', 'G:/ASE1/ase1_prj'])
74/1: my_string[2:5][1]
74/2:
my_string = "Please do your assignments. Please! "
len(my_string)
74/3: my_string[2:5][1]
74/4:
# Remember its immutable
my_string.replace('a', 'A')
74/5:
#Accessing by index
my_list = ['Python', 'is', 'still', 'cool']
print(my_list[0])
print(my_list[-1])
74/6:
#Accessing by index
my_list = ['Python', 'is', 'still', 'cool']
print(my_list)
print(my_list[-1])
74/7:
#Accessing by index
my_list = ['Python', 'is', 'still', 'cool']
print(my_list[0])
print(my_list[-1])
74/8:
numbers = [8, 1, 6, 5, 10]
numbers.sort()
print('numbers: {}'.format(numbers))

numbers.sort(reverse=True)
print('numbers reversed: {}'.format(numbers))

words = ['this', 'is', 'a', 'list', 'of', 'words']
words.sort()
print('words: {}'.format(words))
74/9:
numbers = [8, 1, 6, 5, 10]
sorted_numbers = sorted(numbers)
print('numbers: {}, sorted: {}'.format(numbers, sorted_numbers))
74/10: stack = [3, 4, 5]
74/11:
stack.append(6)
print(stack)
74/12: stack.pop()
74/13:
#Deleting a Value
my_dict = {'key1': 'value1', 'key2': 99, 'keyX': 'valueX'}
del my_dict['keyX']
print(my_dict)
# what happens when the key doesn't exist
74/14:
print('is x in xkcd: {}'.format('x' in 'xkcd'))
print('is x in xkcd: {}'.format('x' in ('x',1,True)))
print('is x in xkcd: {}'.format('x' in {'x',1,True}))
print('is x in xkcd: {}'.format('x' in {'x':1,'y':2,'z':3}))
print('is x in xkcd: {}'.format(1 in {'x':1,'y':2,'z':3}.values()))
74/15:
x = set("A Python Tutorial")
print (x)
74/16:
x = set("A Python Tutorial")
print (x)
74/17:
x = set("A Python Tutorial")
print (x)
74/18:
x = set("A Python Tutorial")
print (x)
74/19:
x = set("A Python Tutorial")
print (x)
74/20:
x = set("A Python Tutorial")
print (x)
74/21:
x = set("A Python Tutorial")
print (x)
74/22:
x = set("A Python Tutorial")
print (x)
74/23:
x = set("A Python Tutorial")
print (x)
74/24:
x = set("A Python Tutorial")
print (x)
74/25:
x = set("A Python Tutorial")
print (x)
74/26:
x = set("A Python Tutorial")
print (x)
74/27:
#What happens now??
cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
74/28:
# All immutable objects are allowed (Tuples are immutable)
cities = {("Python","Perl"), ("Paris", "Berlin", "London")}
print (cities)
74/29:
#What happens now??
cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
74/30:
#Sets vs frozen sets (Sets are mutable, frozen sets are not)
cities = set(['Delhi', 'Chennai', 'Hyderabad'])
cities.add('Mumbai')
print(cities)
74/31:
#Sets vs frozen sets (Sets are mutable, frozen sets are not)
cities = set(['Delhi', 'Chennai', 'Hyderabad'])
cities.add('Mumbai')
print(cities)
74/32:
#Sets vs frozen sets (Sets are mutable, frozen sets are not)
cities = set(['Delhi', 'Chennai', 'Hyderabad'])
cities.add('Mumbai')
print(cities)
74/33:
x = {"a","b","c","d","e"}
y = {"b","c"}
z = {"c","d"}
print ("x - y =",x.difference(y))
print ("x - y - z =",x.difference(y).difference(z))
74/34:
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
74/35:
print("popped: {}".format(queue.popleft()))                 # The first to arrive now leaves
print(queue)
74/36:
print("popped: {}".format(queue.pop()))                 
print(queue)
74/37:
print('1 == 0: {}'.format(1 == 0))
print('1 != 0: {}'.format(1 != 0))
print('1 > 0: {}'.format(1 > 0))
print('1 > 1: {}'.format(1 > 1))
print('1 < 0: {}'.format(1 < 0))
print('1 < 1: {}'.format(1 < 1))
print('1 >= 0: {}'.format(1 >= 0))
print('1 >= 1: {}'.format(1 >= 1))
print('1 <= 0: {}'.format(1 <= 0))
print('1 <= 1: {}'.format(1 <= 1))
74/38:
i_am_true = True
i_am_false = False
i_am_empty = []
i_am_3 = 3
print('True and False is: {}'.format(i_am_true and i_am_false))
print('True and 3 is: {}'.format(i_am_true and i_am_3))
print('empty and 3 is: {}'.format(i_am_empty and i_am_3)) #Short circuiting
74/39:
print('True or False is: {}'.format(i_am_true or i_am_false))
print('True or 3 is: {}'.format(i_am_true or i_am_3))
print('empty or 3 is: {}'.format(i_am_empty or i_am_3))
74/40:
my_int_1 = 5
my_int_2 = 10
x = my_int_2 / (my_int_1 or 2)
print(x)
74/41:
print('is x in xkcd: {}'.format('x' in 'xkcd'))
print('is x in xkcd: {}'.format('x' in ('x',1,True)))
print('is x in xkcd: {}'.format('x' in {'x',1,True}))
print('is x in xkcd: {}'.format('x' in {'x':1,'y':2,'z':3}))
print('is x in xkcd: {}'.format(2 in {'x':1,'y':2,'z':3}.values()))
74/42:
print('is x in xkcd: {}'.format('x' in 'xkcd'))
print('is x in xkcd: {}'.format('x' in ('x',1,True)))
print('is x in xkcd: {}'.format('x' in {'x',1,True}))
print('is x in xkcd: {}'.format('x' in {'x':1,'y':2,'z':3}))
print('is x in xkcd: {}'.format(4 in {'x':1,'y':2,'z':3}.values()))
74/43:
print('is x in xkcd: {}'.format('x' in 'xkcd'))
print('is x in xkcd: {}'.format('x' in ('x',1,True)))
print('is x in xkcd: {}'.format('x' in {'x',1,True}))
print('is x in xkcd: {}'.format('x' in {'x':1,'y':2,'z':3}))
print('is x in xkcd: {}'.format(1 in {'x':1,'y':2,'z':3}.values()))
74/44:
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
74/45:
for idx, val in enumerate(my_list):
    print('idx: {}, value: {}'.format(idx, val))
74/46:
my_list = [0,1, 2, 3, 4]
println(enumerate(my_list))
for item in my_list:
    print(item)
74/47:
my_list = [0,1, 2, 3, 4]
print(enumerate(my_list))
for item in my_list:
    print(item)
74/48:
my_dict = {'hacker': True, 'age': 72, 'name': 'John Doe'}
for val in my_dict:
    print(val)
76/1:
def my_first_function():
    print('Hello world!')

print('type: {}'.format(my_first_function))
#calling my function
my_first_function()
76/2:
def my_first_function_with_params(param1, param2):
    print('Hello world! {} and {}'.format(param1, param2))
my_first_function_with_params("Jack","Jill")
76/3:
my_func_result = my_first_function_with_params("Jack","Jill")
print("result:", my_func_result)
76/4:
def my_first_function_which_returns(param1, param2):
    return 'Hello world! {} and {}'.format(param1, param2)
76/5:
my_func_result = my_first_function_which_returns("Jack","Jill")
print("result:", my_func_result)
76/6: my_first_function_which_returns(param2="Jill",param1="Jack")
76/7:
def my_second_function_which_returns(param1, param2, param3):
    return 'Hello world! {} and {} and {}'.format(param1, param2, param3)
76/8: my_second_function_which_returns("Jack",param3="Mark",param2="Jill")
76/9:
#Default arguments
def create_person_info(name, age, job=None, salary=300):
    info = {'name': name, 'age': age, 'salary': salary}
    
    # Add 'job' key only if it's provided as parameter
    if job:  
        info.update(dict(job=job))
        
    return info

person1 = create_person_info('John Doe', 82)  # use default values for job and salary
person2 = create_person_info('Lisa Doe', 22, 'hacker', 10000)
print(person1)
print(person2)
76/10:
def append_if_multiple_of_five(number, magical_list=[]):
    if number % 5 == 0:
        magical_list.append(number)
    return magical_list

print(append_if_multiple_of_five(100))
print(append_if_multiple_of_five(105))
print(append_if_multiple_of_five(123))
print(append_if_multiple_of_five(123, [1,2,3]))
print(append_if_multiple_of_five(123))
76/11: append_if_multiple_of_five.__defaults__
76/12:
f = open("testfile.txt", "r")
print(f.read())
f.close()
76/13:
f = open('testfile.txt', 'w')
f.write("I am writing this")
f.close()
76/14:
f = open("testfile.txt", "r")
print(f.read())
f.close()
76/15:
f = open("testfile.txt", "r")
print(f.read(1))
f.close()
76/16:
f = open("testfile.txt", "r")
print(f.read(1))
f.close()
76/17:
f = open("testfile.txt", "r")
print(f.readline())
f.close()
76/18:
# lets append one more line
f = open("testfile.txt", "a")
f.write("\n")
f.write("one more line! fun!")
f.close()
76/19:
# lets append one more line
f = open("testfile.txt", "a")
f.write("\n")
f.write("one more line! fun!")
f.close()
76/20:
f = open("testfile.txt", "r")
for x in f:
    print ("line: ", x)
f.close()
76/21:
# lets append one more line
f = open("testfile.txt", "a")
f.write("\n")
f.write("one more line! fun!")
f.close()
76/22:
f = open("testfile.txt", "r")
for x in f:
    print ("line: ", x)
f.close()
76/23:
with open("testfile.txt", "w") as f:
    f.write("I am writing this")
    f.write("\n")
    f.write("one more line! fun!")
76/24:
with open("testfile.txt", "r") as f:
    for x in f:
        print ("line: ", x)
76/25:
with open("testfile.txt", "w+")as fo:
    str = fo.read(3)
    print("Read String is : ", str)
    position = fo.tell()
    print ("Current file position : ", position)
    position = fo.seek(0, 0)
    str = fo.read(3);
    print("Again read String is : ", str)
    fo.write(" stuff ")
    fo.seek(0, 0)
    for x in fo:
        print ("line: ", x)
76/26:
def read_and_append(filename):
    res = "Error opening and reading from file:{}".format(filename)
    with open(filename, "r") as file:
        fstr = file.read().split(',')
        if fstr[0] == "upper":
            res = fstr[1].upper()
        elif fstr[0] == "lower":
            res = fstr[1].lower()
        else:
            res = "unsupported operation"
    with open(filename, "a") as file:
        file.write("\n{}".format(res))
76/27: read_and_append("sample.csv")
76/28:
f = open('testfile.txt', 'w')
f.write("I am writing this")
f.close()
76/29:
f = open('testfile.txt', 'w')
f.write("I am writing this")
f.close()
76/30:
f = open("testfile.txt", "r")
print(f.read())
f.close()
76/31:
f = open("testfile.txt", "r")
print(f.read(1))
f.close()
76/32:
f = open("testfile.txt", "r")
print(f.readline())
f.close()
76/33:
# lets append one more line
f = open("testfile.txt", "a")
f.write("\n")
f.write("one more line! fun!")
f.close()
76/34:
f = open("testfile.txt", "r")
for x in f:
    print ("line: ", x)
f.close()
77/1:
print('PyDev console: using IPython 7.2.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
sys.path.extend(['G:\\DBMS\\KnowYourShow\\KYS', 'G:\\Program Files\\JetBrains\\PyCharm 2018.3.1\\helpers\\pycharm', 'G:\\Program Files\\JetBrains\\PyCharm 2018.3.1\\helpers\\pydev'])
if 'setup' in dir(django): django.setup()
import django_manage_shell; django_manage_shell.run("G:/DBMS/KnowYourShow/KYS")
78/1:
print('PyDev console: using IPython 7.2.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['G:\\DBMS\\KnowYourShow', 'G:/DBMS/KnowYourShow'])
79/1: ?
79/2: import imdb
79/3: top = imdb.IMDB().get_top250_movies()
79/4: top = imdb.IMDB()
79/5: ia = imdb.IMDb()
79/6: ia.get_top250_movies()
79/7: imdb.Objects.all()
79/8: imdb.objects.all()
79/9: help
79/10: help(imdb)
79/11: ia
79/12: ia.search_movie('Better')
79/13: dir(imdb)
79/14: imdb.Character()
79/15: a= imdb.Character
79/16: dir(a)
79/17: a = a.absolute_import
79/18: dir(a)
79/19: a = a.__sizeof__
79/20: dir(a)
79/21: a.__call__()
79/22: dir(imdb)
79/23: local()
79/24: locals()
80/1:
print('PyDev console: using IPython 7.2.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['G:\\DBMS\\KnowYourShow', 'G:/DBMS/KnowYourShow'])
81/1: import tvshows.views
81/2: import tvshow.views
81/3: import tvshow.model
81/4: import tvshow.models
81/5: dir(tvshow.models)
81/6: dir(tvshow.models.models)
81/7: dir(tvshow.models.models.indexes)
81/8: dir(tvshow.models.models.indexes.hashlib)
82/1:
print('PyDev console: using IPython 7.2.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
sys.path.extend(['G:\\DBMS\\KnowYourShow\\KYS', 'G:\\Program Files\\JetBrains\\PyCharm 2018.3.1\\helpers\\pycharm', 'G:\\Program Files\\JetBrains\\PyCharm 2018.3.1\\helpers\\pydev'])
if 'setup' in dir(django): django.setup()
import django_manage_shell; django_manage_shell.run("G:/DBMS/KnowYourShow/KYS")
83/1: import wikipedia
83/2: wikipedia.search('Barack')
83/3: wikipedia.page()
83/4: wikipedia.search('Bob Odenkirk')
83/5: wikipedia.page('Bob Odenkirk')
83/6: dir(wikipedia.page('Bob Odenkirk'))
83/7: wikipedia.page('Bob Odenkirk').url
83/8: wikipedia.page('Bob Odenkirk').images
83/9: wikipedia.page('Bob Odenkirk').section
83/10: wikipedia.page('Bob Odenkirk').summary
83/11: wikipedia.page('Bob Odenkirk').section.title
83/12: wikipedia.page('Bob Odenkirk').section(Born)
83/13: wikipedia.page('Bob Odenkirk').section('Born')
83/14: wikipedia.page('Bob Odenkirk').section('Born')
83/15: wikipedia.page('Bob Odenkirk').section('Early Life')
83/16: sections
83/17: wikipedia.WikipediaPage('Bob Odenkirk)
83/18: wikipedia.WikipediaPage('Bob Odenkirk')
83/19: dir(wikipedia.WikipediaPage('Bob Odenkirk'))
83/20: wikipedia.WikipediaPage('Bob Odenkirk').catagories
83/21: wikipedia.WikipediaPage('Bob Odenkirk').categories
83/22: wikipedia.WikipediaPage('Bob Odenkirk').sections
83/23: wikipedia.WikipediaPage('Bob Odenkirk').section
83/24: dir(wikipedia.WikipediaPage('Bob Odenkirk').section)
83/25: wikipedia.WikipediaPage('Bob Odenkirk').sections
83/26: wikipedia.WikipediaPage('India').sections
83/27: wikipedia.WikipediaPage('Barrack Obama').sections
83/28: wikipedia.WikipediaPage('Barrack Obama').content
83/29: wikipedia.page('Bob Odenkirk)
83/30: wikipedia.page('Bob Odenkirk')
83/31: dir(wikipedia.page('Bob Odenkirk'))
83/32: wikipedia.page('Bob Odenkirk').images
83/33: wikipedia.page('Bob Odenkirk').content
83/34: wikipedia.page('Bob Odenkirk').sections
83/35: wikipedia.page('Bob Odenkirk').section
83/36: wikipedia.page('Bob Odenkirk').sections
83/37: wikipedia.page('Bob Odenkirk').summary
83/38: wikipedia.page('Bob Odenkirk').categories
83/39: wikipedia.page('Bob Odenkirk').links
   1: import wptools
   2: a = wptools.page('Bob Odenkirk').get_parse()
   3: a.infobox
   4: a
   5: a.infobox
   6: so = wptools.page('Stack Overflow').get_parse()
   7: so.infobox
   8: dir(so)
   9: so.info
  10: so.get
  11: so.show
  12: so = wptools.page('Stack Overflow')
  13: dir(so)
  14: so.info
  15: so.show
  16: so.get_labels
  17: so.data
  18: a = wptools.page('Bob Odenkirk')
  19: a.get_parse()
  20: a = a.get_parse()
  21: a.infobox
  22: a.infobox['Born']
  23: fela = wptools.page('Fela Kuti').get_parse()
  24: fela.infobox['instrument']
  25: a
  26: a.get_parse()
  27: get_parse()
  28:  page = wptools.page('Gandhi')
  29: page.get_parse()
  30: page.get_parse().infobox
  31: type(page.get_parse())
  32: dir(page.get_parse())
  33: page.get_parse().data
  34: page.get_parse().data['infobox']
  35: s = wptools.page('Bob Odenkirk')
  36: s = wptools.page('Bob Odenkirk').get_parse()
  37: s.data['infobox']
  38: s = wptools.page('Barrack Obama')
  39: s = wptools.page('Barrack Obama').get_parse()
  40: s.data['infobox']
  41: s = wptools.page('Barrack Obama').get_parse().data['infobox']['birth_date']
  42: s.data['infobox']['birth_data']
  43: s
  44: s = wptools.page('Bob Odenkirk').get_parse().data['infobox']['birth_date']
  45: s
  46: s = wptools.page('Narendra Modi').get_parse().data['infobox']['birth_date']
  47: s
  48: s = wptools.page('Emilia Clarke').get_parse().data['infobox']['birth_date']
  49: s
  50: s = wptools.page('Jonathan Levine').get_parse().data['infobox']['birth_date']
  51: s
  52: s = wptools.page('Jonathan Levine').get_parse().data['infobox']
  53: s
  54: s = wptools.page('Barrack Obam').get_parse().data['infobox']
  55: s = wptools.page('Barrack').get_parse().data['infobox']
  56: s
  57: s
  58: s = wptools.page('Barrack Obama').get_parse().data['infobox']
  59: s
  60: s
  61: s = wptools.page('Jonathan Levine').get_parse().data['infobox']
  62: s
  63: s = wptools.page('Vince Gilligan').get_parse().data['infobox']
  64: s
  65: s = wptools.page('Seth Rogen').get_parse().data['infobox']
  66: s
  67: s = wptools.page('Millie Bobby Brown').get_parse().data['infobox']
  68: s
  69: s = wptools.page('Millie Bobby Brown').get_parse().data['infobox']['birth_date']
  70: s
  71: s.group(0).split('|')
  72: s.split('|')
  73: s = wptools.page('Millie Bobby Brown').get_parse().data['infobox']['birth_date'].split('|')
  74: s
  75: s = wptools.page('Barrack Obama').get_parse().data['infobox']['birth_date'].split('|')
  76: s
  77: s = wptools.page('Barrack Obama').get_parse().data['infobox']['birth_date'].split('|','}}')
  78: s = wptools.page('Barrack Obama').get_parse().data['infobox']['birth_date'].split('|')
  79: s
  80: s.split('}}')
  81: import re
  82: re.split('|, }}' , wptools.page('Barrack Obama').get_parse().data['infobox']['birth_date'])
  83: re.split('[| }}]' , wptools.page('Barrack Obama').get_parse().data['infobox']['birth_date'])
  84: re.split('[{{ | }}]' , wptools.page('Barrack Obama').get_parse().data['infobox']['birth_date'])
  85: import readline
  86: %history -f G:/1.py
  87: %history -g -f full_history.py
