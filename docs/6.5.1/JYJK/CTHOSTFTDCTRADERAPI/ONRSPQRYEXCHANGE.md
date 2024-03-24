<p>请求查询交易所响应，当执行ReqQryExchange后，该方法被调用。</p>
<span class="anchor" id="f8eaa8e9-6887-41e3-b67a-07c20dbf3345"></span>
## 1.函数原型
<p>virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1fb22bd7-78cf-4095-add8-26b3fb557071"></span>
## 2.参数
<p>pExchange：交易所</p>
<pre><code>struct CThostFtdcExchangeField
{
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///交易所名称
    TThostFtdcExchangeNameType ExchangeName;
    ///交易所属性
    TThostFtdcExchangePropertyType ExchangeProperty;
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
<span class="anchor" id="d54bdeec-8b83-4f4c-9528-7cdee18587d3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="fbf2145e-5275-4797-83c3-2128185ba0dd"></span>
## 4.FAQ
<p>无</p>
