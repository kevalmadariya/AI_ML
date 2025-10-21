from langchain_text_splitters import CharacterTextSplitter

input = """
Several key algorithms are crucial for mobile operating systems due to the unique constraints of mobile devices—like limited battery life, constrained memory, and reliance on touch and sensor inputs—that are not primary concerns for traditional computer operating systems.1
Here are some algorithms and algorithmic strategies used in mobile OSes but generally not in computer OSes:

3. Sensor Fusion Algorithms 🧭
Smartphones are packed with sensors like accelerometers, gyroscopes, and magnetometers.8 Data from a single sensor is often noisy and inaccurate.
The Algorithm: Sensor Fusion algorithms, most commonly the Kalman Filter or a simpler Complementary Filter, are used at the OS level. These algorithms intelligently combine the data streams from multiple sensors to produce a single, far more accurate and stable estimate of the device's orientation and motion.9 For example, it can combine the gyroscope's fast but drifty rotation data with the accelerometer's slow but stable gravity vector to get a precise, drift-free orientation. This is essential for features like screen auto-rotation, step counting, and augmented reality, and is not a feature of standard computer OSes.
"""

splitter = CharacterTextSplitter(
    separator = "",
    chunk_size = 100,
    chunk_overlap  = 0,
)

result = splitter.split_text(input) 

print(result)