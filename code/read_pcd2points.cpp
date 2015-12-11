#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>

int main (int argc, char** argv)
{
    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZ>);

    // Fill in the cloud data
    pcl::PCDReader reader;
    // Replace the path below with the path where you saved your file
    //reader.read<pcl::PointXYZ> ("table_scene_lms400.pcd", *cloud);
    reader.read<pcl::PointXYZ> ("points_cloud_outliers.pcd", *cloud);
    std::ofstream file_writer("filter_points_outliers.xyz", std::ios::out);

    for (size_t i=0; i < cloud->points.size(); ++i) {
        //std::cout << cloud->points[i].x << std::endl;
        file_writer << cloud->points[i].x << ' ' << cloud->points[i].y << ' ' << cloud->points[i].z << '\n';
    }
}
