<p>请求查询客户通知响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYNOTICE/">ReqQryNotice</a>后，该方法被调用。</p>
<span class="anchor" id="901f6014-e151-4b66-b506-889e618b7d6e"></span>
## 1.函数原型
<p>virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="68b1368e-99cc-410e-8d1f-11c9720d6d26"></span>
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
<span class="anchor" id="c19189e2-4f5d-4ea9-a8f5-275833f00de5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="85e15626-1960-4ab0-94cf-132824c79c8b"></span>
## 4.FAQ
<p>无</p>
