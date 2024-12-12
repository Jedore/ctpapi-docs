<p>请求查询客户通知响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYNOTICE/">ReqQryNotice</a>后，该方法被调用。</p>
<span class="anchor" id="598701e4-16d9-43ba-b4a0-4d71c1b4f2f8"></span>
## 1.函数原型
<p>virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a6177dc1-8f40-4c45-b3f1-dcf7ca37dd50"></span>
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
<span class="anchor" id="9841a2ad-96ea-4354-9ec4-30248fb1fedb"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="47db4180-c7c4-45c2-8f25-686751de2011"></span>
## 4.FAQ
<p>无</p>
