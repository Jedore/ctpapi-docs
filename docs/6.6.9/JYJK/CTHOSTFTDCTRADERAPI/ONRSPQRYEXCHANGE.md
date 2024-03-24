<p>请求查询交易所响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGE/">ReqQryExchange</a>后，该方法被调用。</p>
<span class="anchor" id="30146742-f4c6-4f68-a012-1819e3839e4b"></span>
## 1.函数原型
<p>virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="553a5c4e-1bcc-4d76-b632-807a78b0a43d"></span>
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
<span class="anchor" id="1fdcb130-60d7-452b-912a-cb15bfdb99e7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5ddc2509-1bd1-401d-a5ff-b3fd4b83f48c"></span>
## 4.FAQ
<p>无</p>
