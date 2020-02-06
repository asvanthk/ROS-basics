/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle  nh;

void callback( const std_msgs::Int32& msg){
  digitalWrite(13,msg.data);   // blink the led
}

ros::Subscriber<std_msgs::Int32> sub("blink", &callback );

void setup()
{ 
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
