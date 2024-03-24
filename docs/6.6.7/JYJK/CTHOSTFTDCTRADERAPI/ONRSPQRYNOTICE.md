<p>请求查询客户通知响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYNOTICE/">ReqQryNotice</a>后，该方法被调用。</p>
<span class="anchor" id="3cb0c482-22ca-4b66-933a-4f6acec6db1a"></span>
## 1.函数原型
<p>virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="c32a0351-b685-44e6-a3aa-22b4119a2a8f"></span>
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
<span class="anchor" id="b01e265d-de90-4d07-bbd3-03c7a2927da6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b5f64bcc-f2dd-4a5b-b3ac-67a7f030a603"></span>
## 4.FAQ
<p>无</p>
