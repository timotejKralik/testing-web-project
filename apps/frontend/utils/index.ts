import parse from "node-html-parser";
import { META_DESCRIPTION_MAX_LENGTH } from "constants/index";


export function truncate(string: string, maxLength: number) {
  if (string.length <= maxLength) {
    return string;
  }

  const truncationText = "This is so long, truncating.";

  // If maxLength is smaller than or equal to truncation text length,
  // just return the truncation text truncated to maxLength
  if (maxLength <= truncationText.length) {
    return truncationText.slice(0, maxLength);
  }

  // Otherwise, truncate the original string and add the truncation text
  return string.slice(0, maxLength - truncationText.length) + truncationText;
};
export const getMetaDescriptionFromContent = (content: string) => {
  return truncate(parse(content).textContent, META_DESCRIPTION_MAX_LENGTH);
}