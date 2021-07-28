using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;

#nullable disable

namespace ComicBookTracker.Models
{
    [Table("cbtracker_author")]
    public partial class Author
    {
        public Author()
        {
            //Issues = new HashSet<Issue>();
            //Series = new HashSet<Series>();
        }

        public long Id { get; set; }
        public string Name { get; set; }
        public DateTime Updated { get; set; }
        public DateTime Created { get; set; }
        public bool PullList { get; set; }

        public virtual ICollection<Issue> Issues { get; set; }
        public virtual ICollection<Series> Series { get; set; }
    }
}
