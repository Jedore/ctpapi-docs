<p>请求查询客户通知响应，当执行ReqQryNotice后，该方法被调用。</p>
<span class="anchor" id="adf7ce5d-12dc-4f3e-bbfd-13dfc13c9185"></span>
## 1.函数原型
<p>virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2dc93bbe-c84d-4d1f-8f39-67c5eb878cb0"></span>
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
<span class="anchor" id="0247a717-9a78-4dba-a458-c3903281a6bf"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1a02d09d-398c-4275-88d5-ba592e5f28fd"></span>
## 4.FAQ
<p>无</p>
