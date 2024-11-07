import { QuartzTransformerPlugin } from "../types"
import { findAndReplace } from "mdast-util-find-and-replace"

export const Furigana: QuartzTransformerPlugin = () => {
  return {
    name: "Furigana",
    markdownPlugins() {
      return [
        () => {
          return (tree, _file) => {
            // Match pattern {base|furigana}
            findAndReplace(tree, /\{([^\|]+)\|([^\}]+)\}/g, (_value: string, ...capture: string[]) => {
              const [baseText, furiganaText] = capture
              
              // Return HTML ruby node structure
              return {
                type: "html",
                value: `<ruby>${baseText}<rt>${furiganaText}</rt></ruby>`
              }
            })
          }
        }
      ]
    }
  }
}

// Re-export the plugin
export default Furigana