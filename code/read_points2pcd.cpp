#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>

int main (int argc, char** argv)
{
    std::ifstream file_reader("points.xyz", std::ios::in);
    char line[256] = {0};
    std::vector<float*> points;
    while(file_reader.getline(line, sizeof(line))) {
        std::stringstream word(line);
        float *point = new float[3];
        word >> point[0];
        word >> point[1];
        word >> point[2];
        std::cout << point[0] << "*" << point[1] << "*" << point[2] << std::endl;
        points.push_back(point);
    }
    //for (std::vector<float*>::iterator iter=points.begin(); iter != points.end(); iter++) {
    //    float *tmp = *iter;
    //    std::cout << tmp[0]<<"*"<<tmp[1]<< "*" << tmp[2]<<std::endl;
    //}
    std::vector<float*>::size_type width = points.size();

    pcl::PointCloud<pcl::PointXYZ> cloud;

    // Fill in the cloud data
    cloud.width    = width;
    cloud.height   = 1;
    cloud.is_dense = false;
    cloud.points.resize (cloud.width * cloud.height);

    for (size_t i = 0; i < cloud.points.size (); ++i)
    {
        //cloud.points[i].x = 1024 * rand () / (RAND_MAX + 1.0f);
        //cloud.points[i].y = 1024 * rand () / (RAND_MAX + 1.0f);
        //cloud.points[i].z = 1024 * rand () / (RAND_MAX + 1.0f);
        cloud.points[i].x = points[i][0];
        cloud.points[i].y = points[i][1];
        cloud.points[i].z = points[i][2];
    }

    pcl::io::savePCDFileASCII ("test_pcd.pcd", cloud);
    std::cerr << "Saved " << cloud.points.size () << " data points to test_pcd.pcd." << std::endl;

    for (size_t i = 0; i < cloud.points.size (); ++i)
        std::cerr << "    " << cloud.points[i].x << " " << cloud.points[i].y << " " << cloud.points[i].z << std::endl;

    return (0);
}
