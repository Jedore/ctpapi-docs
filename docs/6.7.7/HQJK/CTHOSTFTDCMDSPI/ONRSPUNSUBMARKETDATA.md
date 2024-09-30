<p>取消订阅行情应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEMARKETDATA/">UnSubscribeMarketData</a>后，调用此接口。</p>
<span class="anchor" id="88ec11dd-095d-4062-ae3b-cdc865ed9f08"></span>
## 1.函数原型
<p>virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0c75e3e9-03a8-4d6d-bd38-d38781c11b05"></span>
## 2.参数
<p>pSpecificInstrument：指定的合约</p>
<pre><code>struct CThostFtdcSpecificInstrumentField
{
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<span class="anchor" id="453363c3-34fb-4e68-921c-3b3634ca919a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f3b2ee4b-99bf-49ee-9808-8e9a3b7370ba"></span>
## 4.FAQ
<p>无</p>
