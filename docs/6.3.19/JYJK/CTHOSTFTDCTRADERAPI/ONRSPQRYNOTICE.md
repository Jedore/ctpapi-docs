<p>请求查询客户通知响应，当执行ReqQryNotice后，该方法被调用。</p>
<span class="anchor" id="bc10da9a-c91e-4612-aea0-36c60b472f50"></span>
## 1.函数原型
<p>virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7ec265e7-9537-4e6e-b505-90f76ba66688"></span>
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
<span class="anchor" id="33dc9e57-dfec-4a68-b3fb-bf9438e42129"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e30aa3e8-5298-4ee8-ace9-4090facfe04b"></span>
## 4.FAQ
<p>无</p>
