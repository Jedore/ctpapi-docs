<p>请求查询客户通知响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYNOTICE/">ReqQryNotice</a>后，该方法被调用。</p>
<span class="anchor" id="a7fa4f66-ef26-4a0d-989c-1eb7cb9efee6"></span>
## 1.函数原型
<p>virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6d52da7b-bbdd-4ac5-8813-97337fbea59b"></span>
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
<span class="anchor" id="6cff59fe-40b3-4bc1-aee7-feb1104ca947"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="be0cf101-5d3a-47fc-bf8f-3ef2a8435ba3"></span>
## 4.FAQ
<p>无</p>
