<p>请求查询客户通知响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYNOTICE/">ReqQryNotice</a>后，该方法被调用。</p>
<span class="anchor" id="10bc591b-daa1-41b7-b2cd-d16cee00996c"></span>
## 1.函数原型
<p>virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="06f4d137-4acc-4700-9d06-7250b21437df"></span>
## 2.参数
<p>pNotice：客户通知</p>
<pre><code>struct CThostFtdcNoticeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///消息正文
    TThostFtdcContentType Content;
    ///经纪公司通知内容序列号
    TThostFtdcSequenceLabelType SequenceLabel;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="5ba58f57-a5fe-4eae-b76d-867c8bc22cf4"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="dce9711a-90bd-4485-b38d-61cd18bc5180"></span>
## 4.FAQ
<p>无</p>
