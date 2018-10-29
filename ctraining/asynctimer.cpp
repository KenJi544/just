#include <iostream>
#include <boost/asio.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>

/*Using asio's asynchronous functionality means having a callback function
 * that will be called when an asynchronous operation completes
 */

void print(const boost::system::error_code& /*e*/){
    std::cout<<"hello world\n";
}

int main(){
    boost::asio::io_service io;

    boost::asio::deadline_timer t(io, boost::posix_time::seconds(2));

    //instead of doing a blocking wait 
    //call the deadline_timer::async_wait() function to perform
    //an asynchronous wait
    t.async_wait(&print);

    io.run();
}
