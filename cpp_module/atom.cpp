#include <string>
#include <tuple>



// This file was generated with assistance from ChatGPT.



class Atom {
public:
    std::string symbol;
    int z;
    double mass;
    double r_single;
    double r_double;
    std::tuple<double, double, double> coords;

    Atom(std::string sym, int atomic_number, double x=0.0, double y=0.0, double z_coord=0.0)
        : symbol(sym), z(atomic_number), coords(std::make_tuple(x,y,z_coord))
    {
        // minimal example: set mass and radii for H and C
        if (symbol == "h") { mass = 1.008; r_single=0.31; r_double=0.0; }
        else if (symbol == "c") { mass = 12.011; r_single=0.76; r_double=0.67; }
        else { mass=0; r_single=0; r_double=0; }
    }

    void set_coords(double x, double y, double z_coord) {
        coords = std::make_tuple(x,y,z_coord);
    }
};

