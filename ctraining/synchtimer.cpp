#include <iostream>
#include <boost/asio.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>

int main(){

    //All programs that use asio need to have at least one io_service object
    boost::asio::io_service io;

    /*The core asio classes that provide I/O functionality
     * (or as in this case timer functionality) always take a reference to an 
     * io_service as their first constructor argument. The second argument to 
     * the constructor sets the timer to expire 2 seconds from now.
     */
    std::cout<<"start the timer\n";
    boost::asio::deadline_timer t(io, boost::posix_time::seconds(2));

    //In this simple example we perform a blocking wait on the timer
    t.wait();
    std::cout<<"hello world\n";
}
