<p>请求查询合约响应，当执行ReqQryInstrument后，该方法被调用。</p>
<span class="anchor" id="d050c786-a884-481b-95ce-b475e4dd5dd5"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="66465b91-4b8d-49ca-84b0-b14376e2892a"></span>
## 2.参数
<p>pInstrument：合约</p>
<pre><code>struct CThostFtdcInstrumentField
{
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约名称
    TThostFtdcInstrumentNameType InstrumentName;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///产品代码
    TThostFtdcInstrumentIDType ProductID;
    ///产品类型
    TThostFtdcProductClassType ProductClass;
    ///交割年份
    TThostFtdcYearType DeliveryYear;
    ///交割月
    TThostFtdcMonthType DeliveryMonth;
    ///市价单最大下单量
    TThostFtdcVolumeType MaxMarketOrderVolume;
    ///市价单最小下单量
    TThostFtdcVolumeType MinMarketOrderVolume;
    ///限价单最大下单量
    TThostFtdcVolumeType MaxLimitOrderVolume;
    ///限价单最小下单量
    TThostFtdcVolumeType MinLimitOrderVolume;
    ///合约数量乘数
    TThostFtdcVolumeMultipleType VolumeMultiple;
    ///最小变动价位
    TThostFtdcPriceType PriceTick;
    ///创建日
    TThostFtdcDateType CreateDate;
    ///上市日
    TThostFtdcDateType OpenDate;
    ///到期日
    TThostFtdcDateType ExpireDate;
    ///开始交割日
    TThostFtdcDateType StartDelivDate;
    ///结束交割日
    TThostFtdcDateType EndDelivDate;
    ///合约生命周期状态
    TThostFtdcInstLifePhaseType InstLifePhase;
    ///当前是否交易
    TThostFtdcBoolType IsTrading;
    ///持仓类型
    TThostFtdcPositionTypeType PositionType;
    ///持仓日期类型
    TThostFtdcPositionDateTypeType PositionDateType;
    ///多头保证金率
    TThostFtdcRatioType LongMarginRatio;
    ///空头保证金率
    TThostFtdcRatioType ShortMarginRatio;
    ///是否使用大额单边保证金算法
    TThostFtdcMaxMarginSideAlgorithmType MaxMarginSideAlgorithm;
    ///基础商品代码
    TThostFtdcInstrumentIDType UnderlyingInstrID;
    ///执行价
    TThostFtdcPriceType StrikePrice;
    ///期权类型
    TThostFtdcOptionsTypeType OptionsType;
    ///合约基础商品乘数
    TThostFtdcUnderlyingMultipleType UnderlyingMultiple;
    ///组合类型
    TThostFtdcCombinationTypeType CombinationType;
};
</code></pre>
<p>VolumeMultiple：合约乘数（同交易所）</p>
<p>PriceTick：最小变动价位（同交易所）</p>
<p>IsTrading：是否活跃（同交易所）</p>
<p>DeliveryYear：交割年份（同交易所）</p>
<p>DeliveryMonth：交割月（同交易所）</p>
<p>OpenDate：上市日（同交易所）</p>
<p>CreateDate：创建日（同交易所）</p>
<p>ExpireDate：到期日（同交易所）</p>
<p>StartDeliveDate：开始交割日（同交易所）</p>
<p>EndDelivDate：结束交割日（同交易所）</p>
<blockquote>
<p><code>同交易所</code>表示这些字段每天更新自交易所，其余字段为柜台设置值。如果发现有些字段值有误，则以此来判断是交易所问题还是CTP柜台设置问题。</p>
</blockquote>
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
<span class="anchor" id="60db240b-9647-466b-99fd-70a21b529e93"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="fa77d9ca-90cc-40f8-b71b-677473066957"></span>
## 4.FAQ
<p>无</p>
