<p>请求查询交易所响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGE/">ReqQryExchange</a>后，该方法被调用。</p>
<span class="anchor" id="17666895-43a0-4986-b528-4db42e682800"></span>
## 1.函数原型
<p>virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f9d40883-234b-4369-ade0-5934e6f1ec2e"></span>
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
<span class="anchor" id="021f7ba8-b04e-4fee-a7f0-64b331472d70"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9340085e-b356-4728-a251-012afde543bc"></span>
## 4.FAQ
<p>无</p>
