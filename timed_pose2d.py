class timed_pose2d:
    def __init__(self,x,y,th,time_abs,time_rel) -> None:
        """
        Pose object with time
        time_abs is the abosolute time (i.e. ROS time)
        time_rel is the relative time (from a ref timestamp)
        """
        self.x=x
        self.y=y
        self.th=th
        self.time_abs=time_abs
        self.time_rel=time_rel