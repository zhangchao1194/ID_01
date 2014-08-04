#ifndef VISUALIZE_HPP_
#define VISUALIZE_HPP_
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <string>
#include <vector>
#include "Candidate.hpp"
#include "types.hpp"

/*! @class Visualize
 *  @brief visualize detection candidates
 *
 * visualize a collection of object detection candidates by rendering the
 * input image to screen, and overlaying the detection bounding boxes of
 * each of the parts, with optional confidence values
 */
class Visualize {
private:
	//! the name of the OpenCV window
	std::string name_;
public:
	Visualize() : name_("frame") {}
	Visualize(std::string name) : name_(name) {}
	virtual ~Visualize() {}
	// public methods
	void candidates(const cv::Mat& im, const vectorCandidate& candidates, cv::Mat& canvas, bool display_confidence = false) const;
	void candidates(const cv::Mat& im, const vectorCandidate& candidates, size_t N, cv::Mat& canvas, bool display_confidence = false) const;
	void candidates(const cv::Mat& im, const Candidate& candidate, cv::Mat& canvas, bool display_confidence = true) const;
	void image(const cv::Mat& im) const;
};

#endif /* VISUALIZE_HPP_ */
