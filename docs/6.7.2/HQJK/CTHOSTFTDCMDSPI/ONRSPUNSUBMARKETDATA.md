<p>取消订阅行情应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEMARKETDATA/">UnSubscribeMarketData</a>后，调用此接口。</p>
<span class="anchor" id="b32c7b07-5787-419a-b99f-2f5872fee7d7"></span>
## 1.函数原型
<p>virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="25a47a78-226e-4f5c-898b-26cb5cd233bb"></span>
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
<span class="anchor" id="11c4e32e-ecf0-40cf-8372-39225794ae14"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="88035be9-37cc-4ee5-8783-4fce15c9a19f"></span>
## 4.FAQ
<p>无</p>
