using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;

#nullable disable

namespace ComicBookTracker.Models
{
    [Table("cbtracker_tag")]
    public partial class Tag : BaseModel
    {
        public Tag()
        {
        }

        public long Id { get; set; }
        public string Name { get; set; }
      
        public virtual ICollection<IssueTag> IssueTags { get; set; }
        public virtual ICollection<Issue> Issues { get; set; }

        public virtual ICollection<SeriesTag> SeriesTags { get; set; }
        public virtual ICollection<Series> Series { get; set; }

        public override string ToString()
        {
            return Name;
        }
    }
}
