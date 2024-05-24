import numpy as np
from timed_pose2d import timed_pose2d

# Function to interpolate between two angles (yaw)
def interpolate_th(th1, th2, t):
    angle_diff = np.arctan2(np.sin(th2 - th1), np.cos(th2 - th1))
    return th1 + t * angle_diff

def interpolate_pose(from_pose:timed_pose2d, to_pose:timed_pose2d, target_time):
    if not (from_pose.time_abs <= target_time <= to_pose.time_abs):
        raise ValueError("Target time is outside the interval of the provided poses.")

    # Compute the interpolation factor
    t_factor = (target_time - from_pose.time_abs) / (to_pose.time_abs - from_pose.time_abs)

    # Interpolate x and y
    x = np.interp(target_time, [from_pose.time_abs, to_pose.time_abs], [from_pose.x, to_pose.x])
    y = np.interp(target_time, [from_pose.time_abs, to_pose.time_abs], [from_pose.y, to_pose.y])

    # Interpolate th (yaw)
    th = interpolate_th(from_pose.th, to_pose.th, t_factor)

    # Create and return the interpolated pose
    interpolated_pose = timed_pose2d(x=x, y=y, th=th, time_abs=target_time, time_rel=target_time - from_pose.time_abs)
    return interpolated_pose


#test poses
# Example usage
pose1 = timed_pose2d(x=1.0, y=2.0, th=0.1, time_abs=1.0, time_rel=1.0)
pose2 = timed_pose2d(x=4.0, y=6.0, th=1.2, time_abs=3.0, time_rel=3.0)

# Define the target time for interpolation
target_time = 2.0

for t in range(20):
    temp_time = 1.0 + (0.1*t)

    # Get the interpolated pose
    ipose = interpolate_pose(pose1, pose2, temp_time)

    # Print the interpolated pose
    print(f"Time: {ipose.time_abs}, x: {ipose.x}, y: {ipose.y}, th: {ipose.th}, time_rel: {ipose.time_rel}")