<p>请求查询产品响应，当执行ReqQryProduct后，该方法被调用。</p>
<span class="anchor" id="bc6ccd67-024e-4f4b-b33a-634dafdd8839"></span>
## 1.函数原型
<p>virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="60a9fda4-6e74-4fc1-b1df-b60c63f1a5f9"></span>
## 2.参数
<p>pProduct：产品</p>
<pre><code>struct CThostFtdcProductField
{
    ///产品代码
    TThostFtdcInstrumentIDType ProductID;
    ///产品名称
    TThostFtdcProductNameType ProductName;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///产品类型
    TThostFtdcProductClassType ProductClass;
    ///合约数量乘数
    TThostFtdcVolumeMultipleType VolumeMultiple;
    ///最小变动价位
    TThostFtdcPriceType PriceTick;
    ///市价单最大下单量
    TThostFtdcVolumeType MaxMarketOrderVolume;
    ///市价单最小下单量
    TThostFtdcVolumeType MinMarketOrderVolume;
    ///限价单最大下单量
    TThostFtdcVolumeType MaxLimitOrderVolume;
    ///限价单最小下单量
    TThostFtdcVolumeType MinLimitOrderVolume;
    ///持仓类型
    TThostFtdcPositionTypeType PositionType;
    ///持仓日期类型
    TThostFtdcPositionDateTypeType PositionDateType;
    ///平仓处理类型
    TThostFtdcCloseDealTypeType CloseDealType;
    ///交易币种类型
    TThostFtdcCurrencyIDType TradeCurrencyID;
    ///质押资金可用范围
    TThostFtdcMortgageFundUseRangeType MortgageFundUseRange;
    ///交易所产品代码
    TThostFtdcInstrumentIDType ExchangeProductID;
    ///合约基础商品乘数
    TThostFtdcUnderlyingMultipleType UnderlyingMultiple;
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
<span class="anchor" id="8a735c7b-8d43-43fb-8c2d-03d7f47d4a05"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5d9a7cfb-6d19-450a-b369-acb9ceebf7da"></span>
## 4.FAQ
<p>无</p>
