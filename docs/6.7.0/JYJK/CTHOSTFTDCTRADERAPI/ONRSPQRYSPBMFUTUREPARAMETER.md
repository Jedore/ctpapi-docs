<p>请求SPBM期货合约参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMFUTUREPARAMETER/">ReqQrySPBMFutureParameter</a>后，该方法被调用。</p>
<span class="anchor" id="9bc193b2-096e-42e9-a363-ea48a982d9f0"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMFutureParameter(CThostFtdcSPBMFutureParameterField *pSPBMFutureParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7d5d6fb3-f345-404b-a386-b944bcc95ab7"></span>
## 2.参数
<p>pSPBMFutureParameter：SPBM期货合约保证金参数</p>
<pre><code>struct CThostFtdcSPBMFutureParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///期货合约因子
    TThostFtdcVolumeMultipleType    Cvf;
    ///阶段标识
    TThostFtdcTimeRangeType TimeRange;
    ///品种保证金标准
    TThostFtdcRatioType MarginRate;
    ///期货合约内部对锁仓费率折扣比例
    TThostFtdcRatioType LockRateX;
    ///提高保证金标准
    TThostFtdcRatioType AddOnRate;
    ///昨结算价
    TThostFtdcPriceType PreSettlementPrice;
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
<span class="anchor" id="9aa104ae-9e69-4dc2-8fb6-3ee36333767a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1014a54b-6deb-4864-8c97-0cf92b5cd9c0"></span>
## 4.FAQ
<p>无</p>
