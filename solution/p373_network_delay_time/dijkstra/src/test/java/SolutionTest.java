import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class SolutionTest {
    private Solution solution;

    @BeforeEach
    void setUp() {
        solution = new Solution();
    }

    @Test
    void networkDelayTime() {
        // given
        int[][] times = new int[3][3];
        times[0] = new int[]{2, 1, 1};
        times[1] = new int[]{2, 3, 1};
        times[2] = new int[]{3, 4, 1};
        int n = 4;
        int k = 2;

        // when
        int actual = solution.networkDelayTime(times, n, k);

        // then
        int expected = 2;
        assertThat(actual).isEqualTo(expected);
    }
}
