using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;

#nullable disable

namespace ComicBookTracker.Models
{
    [Table("cbtracker_issue_tags")]
    public partial class IssueTag
    {
        public long Id { get; set; }

        [Column("issue_id")]
        public long IssueId { get; set; }

        [Column("tag_id")]
        public long TagId { get; set; }

        public virtual Issue Issue { get; set; }
        public virtual Tag Tag { get; set; }
    }
}
