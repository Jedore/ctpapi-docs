<p>请求查询交易所响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGE/">ReqQryExchange</a>后，该方法被调用。</p>
<span class="anchor" id="c9dc1f6b-61dc-4e56-a073-b4ce32127ccd"></span>
## 1.函数原型
<p>virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="cee8bf99-e21c-473b-ad0f-e940879bd048"></span>
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
<span class="anchor" id="cfa116f1-f8d6-4137-b18a-9c74885a3f66"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7f6beb3d-42c9-43ee-8bfb-ade488e0bf6a"></span>
## 4.FAQ
<p>无</p>
