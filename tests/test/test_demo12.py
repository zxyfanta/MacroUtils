# -*- coding: utf-8 -*-
import test_utils


DEMO_ID = test_utils.demo_id(__file__)


def test_write_summary():
    test_utils.assert_summary_contents_by_demo(DEMO_ID)


def test_channel_part_surfaces_count():
    test_utils.assert_part_surfaces_count(DEMO_ID, 'Channel', 6)


def test_cylinder_part_surfaces_count():
    test_utils.assert_part_surfaces_count(DEMO_ID, 'Cylinder', 3)


def test_subtract_part_surfaces_count():
    test_utils.assert_part_surfaces_count(DEMO_ID, 'Subtract', 7)


def test_cell_count():
    test_utils.assert_cell_count(DEMO_ID, 18118)


def test_solution():
    test_utils.assert_iteration(DEMO_ID, 14400)
    test_utils.assert_time(DEMO_ID, 12.0)


def test_cfl_avg_report():
    test_utils.assert_report(DEMO_ID, 'CFL_avg', 0.577062)


def test_cfl_max_report():
    test_utils.assert_report(DEMO_ID, 'CFL_max', 8.586637)


def test_time_report():
    test_utils.assert_report(DEMO_ID, 'Time', 12.0, tolerance=0,
                             relative=False)


def test_fx_report():
    test_utils.assert_report(DEMO_ID, 'Fx', 1.036690e-03)


def test_fy_report():
    test_utils.assert_report(DEMO_ID, 'Fy', -7.432943e-04)


def test_scalar_min():
    test_utils.assert_scene_min(DEMO_ID, 'Scalar', 'Scalar', 0.0)


def test_scalar_max():
    test_utils.assert_scene_max(DEMO_ID, 'Scalar', 'Scalar', 0.4,
                                tolerance=0, relative=False)


if __name__ == "__main__":
    pass
